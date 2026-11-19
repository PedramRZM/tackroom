"""Exercise the installed Dream entry points against isolated local histories."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'template/.agents/skills/dream/scripts'


class DreamTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.project = self.root / 'repo'
        self.project.mkdir()
        subprocess.run(['git', 'init', '-q', self.project], check=True)
        inbox = self.project / '.agents/memory/inbox.md'
        inbox.parent.mkdir(parents=True)
        inbox.write_text('# Inbox\n')
        subprocess.run(['git', '-C', self.project, 'add', '.'], check=True)
        subprocess.run(['git', '-C', self.project, '-c', 'user.email=test@example.org',
                        '-c', 'user.name=Test', 'commit', '-qm', 'fixture'], check=True)
        self.env = {**os.environ, 'CODEX_HOME': str(self.root/'codex'), 'CLAUDE_CONFIG_DIR': str(self.root/'claude')}
        self.state = self.root / 'state'
        self.cli = self.root / 'fake-codex'
        self.cli.write_text("""#!/usr/bin/env python3
import json,sys
from pathlib import Path
p=sys.argv
assert '--ephemeral' in p and p[p.index('--sandbox')+1]=='read-only'
if Path('session.txt').exists():result={'summary':'observed','lessons':[]}
else:result={'files':[{'name':'fixture.md','content':'draft'}],'report':'Review pending.'}
Path(p[p.index('--output-last-message')+1]).write_text(json.dumps(result))
""")
        self.cli.chmod(0o700)

    def session(self, name, cwd, age=800, complete=True):
        file = self.root/'codex/sessions'/('rollout-'+name+'.jsonl')
        file.parent.mkdir(parents=True, exist_ok=True)
        items = [('session_meta', {'id':name, 'cwd':str(cwd)}),
                 ('event_msg', {'type':'task_started'}),
                 ('response_item', {'type':'reasoning','text':'private reasoning canary'}),
                 ('response_item', {'type':'message','role':'user','content':[{'type':'input_text','text':'Check this task'}]}),
                 ('response_item', {'type':'custom_tool_call','name':'shell','call_id':'a','input':'example'}),
                 ('response_item', {'type':'custom_tool_call_output','call_id':'a','output':'API_TOKEN=synthetic-secret-test'}),
                 ('event_msg', {'type':'task_complete' if complete else 'task_started'})]
        file.write_text('\n'.join(json.dumps({'type':t,'payload':v}) for t,v in items))
        stamp=time.time()-age
        os.utime(file,(stamp,stamp))

    def invoke(self, tool, *options, check=True):
        return subprocess.run([sys.executable, SCRIPTS/tool, *options],cwd=self.project,env=self.env,
                              capture_output=True,text=True,check=check)

    def test_export_without_claude_scopes_codex_and_redacts(self):
        sub=self.project/'src';sub.mkdir()
        self.session('one',sub)
        self.session('other',self.root)
        self.session('active',self.project,age=0)
        self.session('unfinished',self.project,complete=False)
        self.invoke('export-transcripts.py')
        files=list((self.project/'.agents/memory/.transcripts').glob('*.txt'))
        self.assertEqual(len(files),1)
        content=files[0].read_text()
        self.assertIn('TOOL RESULT (shell)',content)
        self.assertNotIn('synthetic-secret-test',content)
        self.assertNotIn('private reasoning',content)

    def test_queue_survives_failure_and_limit_without_editing_project(self):
        for name in ['one','two']:
            self.session(name,self.project)
        args=['run','--state',self.state,'--limit','1']
        self.assertNotEqual(self.invoke('scheduled-dream.py',*args,'--codex','/bin/false',check=False).returncode,0)
        self.assertEqual(len(list((self.state/'queue').glob('*.txt'))),2)
        for _ in range(3):
            self.invoke('scheduled-dream.py',*args,'--codex',self.cli)
        reports=list((self.state/'runs').glob('*/manifest.json'))
        self.assertEqual(len(reports),2)
        ids={json.loads(p.read_text())['analyzed'][0] for p in reports}
        self.assertEqual(len(ids),2)
        self.assertFalse((self.project/'.agents/memory/fixture.md').exists())
        self.assertEqual(list((self.state/'queue').glob('*.txt')),[])


if __name__ == '__main__':
    unittest.main()

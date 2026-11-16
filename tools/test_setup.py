"""Installer behavior through its public CLI, using disposable projects."""
import contextlib
import copy
import importlib.machinery
import io
import json
import os
import shutil
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from unittest.mock import patch
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SETUP = ROOT / "tools/setup"


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="tackroom-install-test-")
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)

    def run_setup(self, *args, ok=True):
        result = subprocess.run([sys.executable, str(SETUP), *args], cwd=self.project,
                                text=True, capture_output=True)
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def test_codex_base_without_other_agents_or_ui(self):
        self.run_setup("--agents", "codex", "--tracker", "files")
        self.assertTrue((self.project / ".codex/config.toml").is_file())
        self.assertTrue((self.project / ".agents/skills/verify/SKILL.md").is_file())
        self.assertFalse((self.project / ".claude").exists())
        self.assertFalse((self.project / ".opencode").exists())
        self.assertFalse((self.project / ".agents/skills/ui-craft").exists())

    def test_ui_profile_includes_resources(self):
        self.run_setup("--agents", "claude", "--profile", "ui")
        self.assertTrue((self.project / ".agents/skills/ui-craft/references/motion.md").is_file())
        self.assertEqual((self.project / ".claude/skills/ui-craft").resolve(),
                         self.project / ".agents/skills/ui-craft")

    def test_selection_required(self):
        result = self.run_setup(ok=False)
        self.assertIn("--agents", result.stderr)
        self.assertEqual(list(self.project.iterdir()), [])



setup = importlib.machinery.SourceFileLoader('installer_tests', str(SETUP)).load_module()
render = importlib.machinery.SourceFileLoader('renderer_tests', str(ROOT / 'tools/render-harness')).load_module()


def snapshot(root):
    result = {}
    for p in root.rglob('*'):
        rel = p.relative_to(root).as_posix()
        if p.is_symlink():
            result[rel] = ('link', os.readlink(p))
        elif p.is_file():
            result[rel] = (p.stat().st_mode & 0o777, p.read_bytes())
        elif p.is_dir():
            result[rel] = ('directory',)
    return result


class PreservationTests(SetupTests):
    def test_all_agents_and_individual_selection(self):
        for agents in ('claude', 'codex', 'opencode', 'claude,codex,opencode'):
            with self.subTest(agents=agents), tempfile.TemporaryDirectory() as directory:
                project = Path(directory)
                self.run_setup(directory, '--agents', agents, '--profile', 'ui', '--tracker', 'issues')
                self.assertEqual((project / '.claude').exists(), 'claude' in agents)
                self.assertEqual((project / '.codex').exists(), 'codex' in agents)
                self.assertEqual((project / '.opencode').exists(), 'opencode' in agents)
                self.assertTrue((project / '.github/ISSUE_TEMPLATE/task.yml').is_file())
                self.assertFalse((project / 'tasks').exists())
                self.assertTrue(os.access(project / '.agents/hooks/session-context.sh', os.X_OK))
                for p in project.rglob('*'):
                    if p.is_symlink():
                        self.assertTrue(p.exists(), p)
                if 'codex' in agents:
                    self.assertNotIn('.claude/', (project / '.codex/hooks.json').read_text())

    def test_dry_run_matches_actual_and_rerun(self):
        before = snapshot(self.project)
        dry = self.run_setup('--agents', 'codex', '--profile', 'ui', '--dry-run')
        self.assertEqual(snapshot(self.project), before)
        real = self.run_setup('--agents', 'codex', '--profile', 'ui')
        planned = [line.replace('would ', '') for line in dry.stdout.splitlines() if 'would add:' in line]
        actual = [line for line in real.stdout.splitlines() if '  add:' in line]
        self.assertEqual(planned, actual)
        before = snapshot(self.project)
        self.run_setup('--update')
        self.assertEqual(snapshot(self.project), before)

    def test_invalid_inputs_do_not_write(self):
        for flags in (('--agents', 'unknown'), ('--agents', 'codex', '--skills', 'oops'),
                      ('--agents', 'codex', '--profile', 'oops'), ('--agents', 'codex', '--legacy')):
            self.run_setup(*flags, ok=False)
            self.assertEqual(snapshot(self.project), {})

    def test_catalog_listing(self):
        result = self.run_setup('--list')
        self.assertIn('ui-craft: optional', result.stdout)
        self.assertIn('Profile ui:', result.stdout)
        self.assertEqual(snapshot(self.project), {})

    def test_custom_data_and_conflicts(self):
        files = {'AGENTS.md': 'my instructions', '.agents/memory/_index.md': 'my memory',
                 '.agents/dream-report.md': 'my report', '.agents/memory/.transcripts/session.txt': 'transcript',
                 'docs/notes.md': 'project notes', '.agents/skills/verify/SKILL.md': 'local verification'}
        for rel, data in files.items():
            p = self.project / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(data)
        result = self.run_setup('--agents', 'codex', ok=False)
        self.assertEqual(result.returncode, 2)
        self.assertTrue((self.project / '.codex/config.toml').exists())
        self.run_setup('--update', ok=False)
        for rel, data in files.items():
            self.assertEqual((self.project / rel).read_text(), data)
        state = json.loads((self.project / setup.STATE).read_text())
        self.assertNotIn('AGENTS.md', state['files'])

    def test_escaping_parent_and_ignore_link(self):
        for rel in ('.agents', '.gitignore'):
            with tempfile.TemporaryDirectory() as outside:
                path = self.project / rel
                path.symlink_to(outside)
                before = snapshot(self.project)
                result = self.run_setup('--agents', 'codex', ok=False)
                self.assertIn('escapes project', result.stderr)
                self.assertEqual(snapshot(self.project), before)
                self.assertEqual(list(Path(outside).iterdir()), [])
                path.unlink()

    def test_legacy_internal_skill_alias_preserved(self):
        old = self.project / '.claude/skills/verify'
        old.mkdir(parents=True)
        (old / 'SKILL.md').write_text('old project skill')
        shared = self.project / '.agents/skills'
        shared.mkdir(parents=True)
        (shared / 'verify').symlink_to('../../.claude/skills/verify')
        result = self.run_setup('--agents', 'claude', ok=False)
        self.assertEqual(result.returncode, 2)
        self.assertEqual((old / 'SKILL.md').read_text(), 'old project skill')
        self.assertTrue((self.project / setup.STATE).is_file())

    def test_internal_alias_cannot_write_into_memory(self):
        memory = self.project / '.agents/memory'
        memory.mkdir(parents=True)
        (memory / 'note.md').write_text('project knowledge')
        (self.project / '.agents/skills').symlink_to('memory')
        before = snapshot(self.project)
        result = self.run_setup('--agents', 'codex', ok=False)
        self.assertIn('aliases project data', result.stderr)
        self.assertEqual(snapshot(self.project), before)

    def test_protected_path_collisions_report_incomplete(self):
        for kind in ('directory', 'dangling-link'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as directory:
                project = Path(directory)
                index = project / '.agents/memory/_index.md'
                index.parent.mkdir(parents=True)
                if kind == 'directory':
                    index.mkdir()
                else:
                    index.symlink_to('missing-index')
                result = self.run_setup(directory, '--agents', 'codex', ok=False)
                self.assertEqual(result.returncode, 2)
                self.assertIn('required file is not readable', result.stdout)
                self.assertTrue(index.is_dir() if kind == 'directory' else index.is_symlink())


class SourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='tackroom-source-test-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.template = self.base / 'source/template'
        shutil.copytree(ROOT / 'template', self.template, symlinks=True, ignore=shutil.ignore_patterns('__pycache__'))
        self.project = self.base / 'app'
        self.project.mkdir()
        self.regenerate()

    def regenerate(self):
        self.catalog, self.generated = render.outputs(self.template)

    def call(self, *args, expected=0):
        output = io.StringIO()
        with patch.object(setup, 'TEMPLATE', self.template), contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            result = setup.main([str(self.project), *args])
        self.assertEqual(result, expected, output.getvalue())
        return output.getvalue()

    def test_update_changes_only_unmodified_harness(self):
        self.call('--agents', 'claude,codex,opencode', '--profile', 'ui')
        custom = self.project / '.agents/skills/verify/SKILL.md'
        custom.write_text('custom local verification')
        protected_files = ['.agents/memory/_index.md', '.agents/memory/inbox.md', 'tasks/README.md', 'docs/decisions/README.md']
        before = {p: (self.project / p).read_bytes() for p in protected_files}
        (self.project / '.agents/dream-report.md').write_text('dream knowledge')
        # Deliberately change upstream even when the installed skeleton was never customized.
        for rel in [*protected_files, '.agents/skills/spec/SKILL.md', '.agents/skills/verify/SKILL.md']:
            path = self.template / rel
            path.write_text(path.read_text() + '\nUpstream update.\n')
        self.regenerate()
        initial = snapshot(self.project)
        self.call('--update', '--dry-run', expected=2)
        self.assertEqual(initial, snapshot(self.project))
        result = self.call('--update', expected=2)
        self.assertIn('update: .agents/skills/spec/SKILL.md', result)
        self.assertIn('conflict (kept local): .agents/skills/verify/SKILL.md', result)
        self.assertEqual(custom.read_text(), 'custom local verification')
        for rel, data in before.items():
            self.assertEqual((self.project / rel).read_bytes(), data)
        self.assertEqual((self.project / '.agents/dream-report.md').read_text(), 'dream knowledge')
        current = snapshot(self.project)
        self.call('--update', expected=2)
        self.assertEqual(current, snapshot(self.project))

    def test_missing_managed_file_restored_but_memory_not_recreated(self):
        self.call('--agents', 'codex')
        (self.project / '.agents/memory/_index.md').unlink()
        (self.project / '.agents/skills/spec/SKILL.md').unlink()
        self.call('--update')
        self.assertFalse((self.project / '.agents/memory/_index.md').exists())
        self.assertTrue((self.project / '.agents/skills/spec/SKILL.md').is_file())

    def test_local_customization_without_upstream_change_is_not_a_conflict(self):
        self.call('--agents', 'codex')
        (self.project / 'AGENTS.md').write_text('project instructions')
        before = snapshot(self.project)
        output = self.call('--update')
        self.assertIn('kept local customization (source unchanged): AGENTS.md', output)
        self.assertEqual(snapshot(self.project), before)

    def test_source_edit_propagates_and_stale_adapter_detected(self):
        self.call('--agents', 'claude,codex,opencode')
        path = self.template / '.agents/briefs/reviewer.md'
        path.write_text(path.read_text() + '\nUnique reviewer requirement.\n')
        _, generated = render.outputs(self.template)
        outputs = {rel: ('file', data.decode()) for rel, data in generated.items()}
        stale = render.reconcile(self.project, outputs, False)
        self.assertEqual(set(stale), {'.claude/agents/reviewer.md', '.codex/agents/reviewer.toml', '.opencode/agents/reviewer.md'})
        self.call('--update')
        for rel in stale:
            self.assertIn('Unique reviewer requirement.', (self.project / rel).read_text())
        self.assertEqual(render.reconcile(self.project, outputs, False), [])
        for directory in ('.claude', '.codex', '.opencode'):
            self.assertFalse((self.template / directory).exists())

    def test_add_skill_in_one_folder_only(self):
        skill = self.template / '.agents/skills/example'
        skill.mkdir()
        (skill / 'SKILL.md').write_text('---\nname: example\ndescription: Example skill\n---\nOne source.\n')
        (skill / 'install.json').write_text(json.dumps({'base': False, 'applies_to': 'Example apps', 'requires': ['verify'], 'profiles': {'example': 'Example apps'}}))
        self.call('--agents', 'claude,codex,opencode', '--profile', 'example')
        self.assertEqual((self.project / '.agents/skills/example/SKILL.md').read_text(), (skill / 'SKILL.md').read_text())
        self.assertEqual((self.project / '.claude/skills/example').resolve(), self.project / '.agents/skills/example')

    def test_broken_customization_is_not_reported_as_success(self):
        self.call('--agents', 'codex')
        (self.project / 'AGENTS.md').unlink()
        (self.project / 'AGENTS.md').symlink_to('missing-instructions.md')
        output = self.call('--update', expected=2)
        self.assertIn('conflict (kept local): AGENTS.md', output)

    def test_catalog_invalid_dependencies_paths_and_resources(self):
        original, _ = render.outputs(self.template)
        for defect in ('unknown', 'cycle', 'missing', 'escape', 'link', 'collision'):
            data = copy.deepcopy(original)
            if defect == 'unknown':
                data['skills']['verify']['requires'] = ['no-such-skill']
            elif defect == 'cycle':
                data['skills']['verify']['requires'] = ['task']
            elif defect == 'missing':
                del data['files']['.agents/skills/verify/SKILL.md']
            elif defect == 'escape':
                data['files']['../escape'] = data['files']['AGENTS.md']
            elif defect == 'link':
                data['files']['.claude/skills/verify']['link'] = '../../../escape'
            else:
                data['files']['.agents'] = data['files']['AGENTS.md']
            with self.subTest(defect=defect), self.assertRaises(ValueError):
                setup.validate_catalog(data)
        (self.template / '.agents/skills/ui-craft/references/motion.md').unlink()
        result = self.call('--agents', 'codex', '--profile', 'ui', expected=1)
        self.assertIn('motion.md', result)
        self.assertEqual(snapshot(self.project), {})

    @contextlib.contextmanager
    def server(self, fault=None):
        template = self.template
        requests = []
        sha = 'a' * 40
        owner = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_GET(self):
                requests.append(self.path)
                if '/commits/' in self.path:
                    if fault == 'revision':
                        self.send_error(404)
                        return
                    # A second branch lookup returns a different commit: clients must resolve once.
                    data = json.dumps({'sha': sha if sum('/commits/' in p for p in requests) == 1 else 'b' * 40}).encode()
                elif '/git/trees/' in self.path:
                    if self.path.endswith(sha):
                        data = json.dumps({'truncated': False, 'tree': [{'path': 'template', 'type': 'tree', 'sha': 'c' * 40}]}).encode()
                    else:
                        tree = []
                        for path in template.rglob('*'):
                            if path.is_file() and '__pycache__' not in path.parts:
                                rel = path.relative_to(template).as_posix()
                                tree.append({'path': rel, 'type': 'blob', 'mode': '100755' if path.stat().st_mode & 0o111 else '100644', 'sha': setup.git_digest(path.read_bytes())})
                        if fault == 'path':
                            tree.append({'path': '../escape', 'type': 'blob', 'mode': '100644', 'sha': 'd' * 40})
                        data = json.dumps({'truncated': fault == 'truncated-tree', 'tree': tree}).encode()
                elif self.path.startswith('/' + setup.REPO + '/' + sha + '/template/'):
                    rel = self.path.split('/template/', 1)[1]
                    if fault == 'missing' and rel.endswith('AGENTS.md'):
                        self.send_error(404)
                        return
                    data = (template / rel).read_bytes()
                    if fault == 'hash' and rel.endswith('AGENTS.md'):
                        data = b'truncated content'
                    if fault == 'catalog' and rel == '.agents/adapters.json':
                        data = b'{broken'
                    if fault == 'disconnect' and rel.endswith('AGENTS.md'):
                        self.send_response(200)
                        self.send_header('Content-Length', str(len(data) + 100))
                        self.end_headers()
                        self.wfile.write(data[:10])
                        self.close_connection = True
                        return
                else:
                    self.send_error(404)
                    return
                self.send_response(200)
                self.send_header('Content-Length', str(len(data)))
                self.end_headers()
                self.wfile.write(data)
        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            url = f'http://127.0.0.1:{server.server_port}'
            with patch.object(setup, 'API', url), patch.object(setup, 'RAW', url):
                yield requests
        finally:
            server.shutdown()
            server.server_close()
            thread.join()

    def test_remote_matches_local_and_resolves_once(self):
        self.call('--agents', 'codex', '--profile', 'ui')
        local = snapshot(self.project)
        other = self.base / 'remote-app'
        other.mkdir()
        self.project = other
        with self.server() as requests:
            self.call('--remote', '--agents', 'codex', '--profile', 'ui')
            self.assertEqual(sum('/commits/' in p for p in requests), 1)
            self.assertTrue(all('/' + 'a' * 40 + '/' in p for p in requests if not p.startswith('/repos/')))
            self.assertFalse(any('/.claude/' in p or '/refs/' in p for p in requests))
            before = snapshot(other)
            self.call('--remote', '--ref', 'a' * 40, '--update')
            self.assertEqual(snapshot(other), before)
        remote = snapshot(other)
        local.pop(setup.STATE)
        remote.pop(setup.STATE)
        self.assertEqual(local, remote)

    def test_failed_remote_fetches_never_change_destination(self):
        self.call('--agents', 'codex')
        before = snapshot(self.project)
        for fault in ('revision', 'missing', 'hash', 'catalog', 'path', 'disconnect', 'truncated-tree'):
            with self.subTest(fault=fault), self.server(fault):
                self.call('--remote', '--update', expected=1)
                self.assertEqual(snapshot(self.project), before)


if __name__ == '__main__':
    unittest.main()

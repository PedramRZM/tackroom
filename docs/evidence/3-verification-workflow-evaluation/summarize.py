#!/usr/bin/env python3
"""Offline report from retained tool events and executable artifact checks; no model calls."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent


def main():
    frozen = json.loads((HERE / "frozen.json").read_text())
    assert all(hashlib.sha256((HERE / p).read_bytes()).hexdigest() == sha
               for p, sha in frozen["files"].items()), "Frozen inputs changed"
    rows = []
    for directory in sorted((HERE / "runs").iterdir()):
        metadata = json.loads((directory / "metadata.json").read_text())
        events = [json.loads(line) for line in (directory / "events.jsonl").read_text().splitlines()]
        completed = [e["item"] for e in events if e["type"] == "item.completed"]
        commands = [i for i in completed if i["type"] == "command_execution"]
        usage = [e["usage"] for e in events if e["type"] == "turn.completed"]
        row = {"run": directory.name, "exit": metadata["exit"], "seconds": metadata["elapsed_seconds"],
               "usage": usage, "command_exits": [i.get("exit_code") for i in commands],
               "failed_commands": [{"command": i["command"], "exit": i.get("exit_code")}
                                   for i in commands if i.get("exit_code") != 0],
               "guidance_lines": sum(i["lines"] for i in metadata["guidance"].values()),
               "guidance_bytes": sum(i["bytes"] for i in metadata["guidance"].values())}
        if (directory / "final").exists():
            checked = subprocess.run(["python3", str(HERE / "score.py"), str(directory / "final")],
                                     capture_output=True, text=True, timeout=15)
            assert checked.returncode == metadata["score_exit"]
            score = json.loads(checked.stdout)
            assert score == json.loads((directory / "score.json").read_text())
            persisted = subprocess.run(["python3", str(HERE / "persistence.py"), str(directory / "final")],
                                       capture_output=True, text=True, timeout=15)
            (directory / "persistence.json").write_text(persisted.stdout)
            row.update({"assertions_passed": sum(v is True for v in score.values()),
                        "assertions_total": len(score),
                        "defects_repaired": sum(all(v is True for k, v in score.items() if k.startswith(prefix))
                                                for prefix in ("bug.", "business.", "ui.", "token.")),
                        "clean_passed": sum(v is True for k, v in score.items() if k.startswith("clean.")),
                        "trivial_passed": score["trivial.exact"] is True,
                        "persistence": json.loads(persisted.stdout), "suite_exits": metadata["suite_exits"]})
            methods = []
            for file in (directory / "final").rglob("test*.py"):
                tree = ast.parse(file.read_text())
                methods.extend(str(file.relative_to(directory / "final")) + ":" + node.name
                               for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
                               and node.name.startswith("test_"))
            row["test_methods"] = methods
            row["final_files"] = sorted(str(f.relative_to(directory / "final"))
                                        for f in (directory / "final").rglob("*")
                                        if f.is_file() and "__pycache__" not in f.parts)
        rows.append(row)
    (HERE / "summary.json").write_text(json.dumps(rows, indent=2) + "\n")
    for row in rows:
        print(row["run"], row["exit"], str(row["seconds"]) + "s",
              str(row.get("assertions_passed", "planning")), row.get("persistence", ""))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Post-freeze supplement: verify commits from a separate SQLite connection."""
import importlib.util
import json
from pathlib import Path
import sqlite3
import sys
import tempfile


def check(root):
    spec = importlib.util.spec_from_file_location("persistence_app", Path(root) / "app.py")
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)
    results = {}
    for role, expected, status in (("approver", True, "approved"), ("viewer", False, "pending")):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "invoices.sqlite"
            first = sqlite3.connect(path)
            try:
                first.execute("CREATE TABLE invoices(id INTEGER PRIMARY KEY, status TEXT)")
                first.execute("INSERT INTO invoices VALUES (1,'pending')")
                first.commit()
                result = app.approve(first, role, 1)
                second = sqlite3.connect(path)
                try:
                    stored = second.execute("SELECT status FROM invoices WHERE id=1").fetchone()[0]
                finally:
                    second.close()
                results[role] = result is expected and stored == status
            finally:
                first.close()
    return results


if __name__ == "__main__":
    results = check(sys.argv[1])
    print(json.dumps(results, indent=2))
    sys.exit(0 if all(results.values()) else 1)

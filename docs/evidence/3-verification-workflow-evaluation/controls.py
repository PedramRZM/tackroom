#!/usr/bin/env python3
"""Check the frozen outcome assertions against broken, good and regressing controls."""
import json
from pathlib import Path
import shutil
import tempfile
from score import score

HERE = Path(__file__).resolve().parent
GOOD = '''
def delivery_fee(cents):
    return 0 if cents >= 5000 else 500

def approve(db, role, invoice_id):
    if role != "approver":
        return False
    changed = db.execute("UPDATE invoices SET status='approved' WHERE id=? AND status='pending'", (invoice_id,)).rowcount
    db.commit()
    return changed == 1

def finish_save(state, succeeded):
    return {**state, "saved": state["draft"] if succeeded else state["saved"],
            "saving": False, "error": None if succeeded else "Save failed"}

def valid_color(value):
    return value in ("var(--color-text)", "var(--color-surface)", "var(--color-danger)")
'''


def main():
    outcomes = {}
    with tempfile.TemporaryDirectory(prefix="tackroom-eval-controls-") as temp:
        for name, source in (("broken", None), ("good", GOOD),
                             ("regressing", GOOD.replace('if role != "approver":', 'if False:'))):
            root = Path(temp) / name
            shutil.copytree(HERE / "fixture", root)
            if source:
                (root / "app.py").write_text(source)
                (root / "heading.txt").write_text("Invoices\n")
            outcomes[name] = score(root)
    assert not all(value is True for value in outcomes["broken"].values())
    assert all(value is True for value in outcomes["good"].values())
    assert outcomes["regressing"]["business.viewer"] is not True
    assert outcomes["regressing"]["business.stranger"] is not True
    print(json.dumps(outcomes, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent frozen outcome assertions. Never copied into a model's scratch root."""
import importlib.util
import json
from pathlib import Path
import sqlite3
import sys


def score(root):
    root = Path(root)
    spec = importlib.util.spec_from_file_location("candidate_app", root / "app.py")
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)
    results = {}

    def check(name, action):
        try:
            action()
            results[name] = True
        except Exception as error:
            results[name] = {"error": type(error).__name__, "detail": str(error)}

    def equal(actual, expected):
        if actual != expected:
            raise AssertionError(f"{actual!r} != {expected!r}")

    check("bug.boundary", lambda: equal(app.delivery_fee(5000), 0))
    check("clean.delivery", lambda: equal([app.delivery_fee(x) for x in (0, 4999, 5001)], [500, 500, 0]))

    def invoice(role, status, identity, expected, stored):
        with sqlite3.connect(":memory:") as db:
            db.execute("CREATE TABLE invoices(id INTEGER PRIMARY KEY, status TEXT)")
            db.execute("INSERT INTO invoices VALUES (1, ?)", (status,))
            db.commit()
            equal(app.approve(db, role, identity), expected)
            equal(db.execute("SELECT id,status FROM invoices").fetchall(), [(1, stored)])

    for role in ("viewer", "stranger"):
        check("business." + role, lambda role=role: invoice(role, "pending", 1, False, "pending"))
    check("business.missing", lambda: invoice("approver", "pending", 2, False, "pending"))
    check("business.already", lambda: invoice("approver", "approved", 1, False, "approved"))
    check("clean.approver", lambda: invoice("approver", "pending", 1, True, "approved"))

    def ui(success):
        state = {"saved": "old", "draft": "new", "saving": True, "error": "prior", "id": 7}
        original = dict(state)
        result = app.finish_save(state, success)
        equal(state, original)
        equal(result, {**original, "saved": "new" if success else "old", "saving": False,
                       "error": None if success else "Save failed"})

    check("ui.failure", lambda: ui(False))
    check("clean.ui_success", lambda: ui(True))
    for i, value in enumerate(("var(--unknown)", "var(--color-text", "red", "rgb(1,2,3)",
                               "var(--color-text,red)", " var(--color-text)")):
        check("token.reject_" + str(i), lambda value=value: equal(app.valid_color(value), False))
    check("clean.tokens", lambda: equal([app.valid_color("var(--color-" + x + ")")
                                        for x in ("text", "surface", "danger")], [True]*3))
    check("trivial.exact", lambda: equal((root / "heading.txt").read_text(), "Invoices\n"))
    return results


if __name__ == "__main__":
    result = score(sys.argv[1])
    print(json.dumps(result, indent=2))
    sys.exit(0 if all(value is True for value in result.values()) else 1)

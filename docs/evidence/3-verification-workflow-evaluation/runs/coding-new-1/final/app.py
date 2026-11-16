"""Small offline exercise; every boundary is local."""


def delivery_fee(cents):
    return 0 if cents >= 5000 else 500


def approve(db, role, invoice_id):
    if role != "approver":
        return False
    cursor = db.execute(
        "UPDATE invoices SET status='approved' WHERE id=? AND status='pending'",
        (invoice_id,),
    )
    if cursor.rowcount == 0:
        return False
    db.commit()
    return True


def finish_save(state, succeeded):
    return {
        **state,
        "saved": state["draft"] if succeeded else state["saved"],
        "saving": False,
        "error": None if succeeded else "Save failed",
    }


def valid_color(value):
    return value in (
        "var(--color-text)",
        "var(--color-surface)",
        "var(--color-danger)",
    )

"""Small offline exercise; every boundary is local."""


def delivery_fee(cents):
    return 0 if cents > 5000 else 500


def approve(db, role, invoice_id):
    db.execute("UPDATE invoices SET status='approved' WHERE id=?", (invoice_id,))
    db.commit()
    return True


def finish_save(state, succeeded):
    return {**state, "saved": state["draft"], "saving": False, "error": None}


def valid_color(value):
    return value.startswith("var(--")

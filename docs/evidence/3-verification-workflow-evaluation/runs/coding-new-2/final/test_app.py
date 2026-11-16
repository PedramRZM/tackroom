import unittest
from app import delivery_fee, valid_color


class Existing(unittest.TestCase):
    def test_delivery(self):
        self.assertEqual(delivery_fee(100), 500)
        self.assertEqual(delivery_fee(6000), 0)

    def test_color(self):
        self.assertTrue(valid_color("var(--color-text)"))
        self.assertFalse(valid_color("#fff"))


class Regression(unittest.TestCase):
    def test_delivery_boundary(self):
        for cents, expected in ((4999, 500), (5000, 0), (5001, 0)):
            with self.subTest(cents=cents):
                self.assertEqual(delivery_fee(cents), expected)

    def test_save_results(self):
        from app import finish_save
        for succeeded in (False, True):
            with self.subTest(succeeded=succeeded):
                state = dict(saved='old', draft='edited', saving=True,
                             error='previous error', extra='preserved')
                original = state.copy()
                result = finish_save(state, succeeded)
                self.assertEqual(result, dict(
                    saved='edited' if succeeded else 'old', draft='edited',
                    saving=False, error=None if succeeded else 'Save failed',
                    extra='preserved'))
                self.assertEqual(state, original)
                self.assertIsNot(result, state)

    def test_color_allowlist(self):
        for value in ('var(--color-text)', 'var(--color-surface)',
                      'var(--color-danger)'):
            with self.subTest(value=value):
                self.assertTrue(valid_color(value))
        for value in ('var(--anything)', 'var(--color-text',
                      'var(--color-text))', 'var(--color-text) trailing',
                      'var(--color-text, red)', 'var( --color-text)',
                      ' var(--color-text)', 'var(--color-text) ',
                      'var(--color-text)\n', '#fff', 'red', 'rgb(0,0,0)', ''):
            with self.subTest(value=value):
                self.assertFalse(valid_color(value))


class Approval(unittest.TestCase):
    def setUp(self):
        import sqlite3
        import tempfile
        from pathlib import Path
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / 'invoices.sqlite'
        self.db = sqlite3.connect(self.path)
        self.addCleanup(self.db.close)
        self.db.execute('CREATE TABLE invoices(id INTEGER PRIMARY KEY, status TEXT)')
        self.db.executemany('INSERT INTO invoices VALUES (?, ?)',
                            [(1, 'pending'), (2, 'approved'), (3, 'cancelled')])
        self.db.commit()

    def persisted(self):
        import sqlite3
        db = sqlite3.connect(self.path)
        try:
            return db.execute('SELECT id, status FROM invoices ORDER BY id').fetchall()
        finally:
            db.close()

    def test_approver_persists_pending_approval(self):
        from app import approve
        self.assertIs(approve(self.db, 'approver', 1), True)
        self.assertEqual(self.persisted(),
                         [(1, 'approved'), (2, 'approved'), (3, 'cancelled')])

    def test_rejected_approvals_leave_storage_unchanged(self):
        from app import approve
        expected = [(1, 'pending'), (2, 'approved'), (3, 'cancelled')]
        for role, invoice_id in (('viewer', 1), ('unknown', 1),
                                 ('approver', 999), ('approver', 2),
                                 ('approver', 3)):
            with self.subTest(role=role, invoice_id=invoice_id):
                self.assertIs(approve(self.db, role, invoice_id), False)
                self.assertEqual(self.persisted(), expected)
                self.assertEqual(self.db.execute(
                    'SELECT id, status FROM invoices ORDER BY id').fetchall(), expected)


if __name__ == "__main__":
    unittest.main()

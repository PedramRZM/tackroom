import unittest
from app import delivery_fee, valid_color


class Existing(unittest.TestCase):
    def test_delivery(self):
        self.assertEqual(delivery_fee(100), 500)
        self.assertEqual(delivery_fee(6000), 0)

    def test_color(self):
        self.assertTrue(valid_color("var(--color-text)"))
        self.assertFalse(valid_color("#fff"))


class DeliveryBoundary(unittest.TestCase):
    def test_free_delivery_threshold(self):
        for cents, expected in [(0, 500), (4999, 500), (5000, 0), (5001, 0)]:
            with self.subTest(cents=cents):
                self.assertEqual(delivery_fee(cents), expected)


class InvoiceApproval(unittest.TestCase):
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
                            [(1, 'pending'), (2, 'approved'), (3, 'draft')])
        self.db.commit()

    def stored_rows(self):
        import sqlite3
        with sqlite3.connect(self.path) as reader:
            return reader.execute('SELECT id, status FROM invoices ORDER BY id').fetchall()

    def test_approver_persists_pending_approval(self):
        from app import approve
        self.assertIs(approve(self.db, 'approver', 1), True)
        self.assertEqual(self.stored_rows(), [(1, 'approved'), (2, 'approved'), (3, 'draft')])

    def test_rejections_leave_storage_unchanged(self):
        from app import approve
        before = self.stored_rows()
        for role, invoice_id in [('viewer', 1), ('unknown', 1), ('approver', 999),
                                 ('approver', None), ('approver', 2), ('approver', 3)]:
            with self.subTest(role=role, invoice_id=invoice_id):
                self.assertIs(approve(self.db, role, invoice_id), False)
                self.assertEqual(self.stored_rows(), before)
                self.assertEqual(self.db.execute('SELECT id, status FROM invoices ORDER BY id').fetchall(), before)


class SaveResult(unittest.TestCase):
    def test_save_results_preserve_input_and_unrelated_fields(self):
        from app import finish_save
        for succeeded in (False, True):
            with self.subTest(succeeded=succeeded):
                state = dict(saved='old', draft='edited', saving=True, error='previous', other=42)
                original = state.copy()
                result = finish_save(state, succeeded)
                self.assertEqual(result, dict(saved='edited' if succeeded else 'old',
                    draft='edited', saving=False, error=None if succeeded else 'Save failed', other=42))
                self.assertEqual(state, original)
                self.assertIsNot(result, state)


class ColorValues(unittest.TestCase):
    def test_exact_allowed_values(self):
        for value in ('var(--color-text)', 'var(--color-surface)', 'var(--color-danger)'):
            with self.subTest(value=value):
                self.assertTrue(valid_color(value))

    def test_other_values_rejected(self):
        for value in ('var(--other)', '#fff', 'red', '', 'var(--color-text',
                      'var(--color-text) trailing', ' var(--color-text)',
                      'var(--color-text)\n', 'var( --color-text)',
                      'var(--color-text, red)', 'VAR(--color-text)'):
            with self.subTest(value=value):
                self.assertFalse(valid_color(value))


if __name__ == "__main__":
    unittest.main()

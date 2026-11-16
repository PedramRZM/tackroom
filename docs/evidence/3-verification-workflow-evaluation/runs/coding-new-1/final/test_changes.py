import copy
import sqlite3
import tempfile
import unittest
from pathlib import Path

from app import approve, delivery_fee, finish_save, valid_color


class DeliveryTests(unittest.TestCase):
    def test_free_delivery_boundary(self):
        for cents, fee in ((4999, 500), (5000, 0), (5001, 0)):
            with self.subTest(cents=cents):
                self.assertEqual(delivery_fee(cents), fee)


class ApprovalTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / 'invoices.sqlite'
        self.db = sqlite3.connect(self.path)
        self.addCleanup(self.db.close)
        self.db.execute('CREATE TABLE invoices(id INTEGER PRIMARY KEY, status TEXT)')
        self.db.executemany('INSERT INTO invoices VALUES (?, ?)',
                            [(1, 'pending'), (2, 'approved'), (3, 'draft')])
        self.db.commit()

    def rows(self):
        with sqlite3.connect(self.path) as reader:
            return reader.execute('SELECT id, status FROM invoices ORDER BY id').fetchall()

    def test_approver_persists_pending_approval(self):
        self.assertIs(approve(self.db, 'approver', 1), True)
        self.assertEqual(self.rows(), [(1, 'approved'), (2, 'approved'), (3, 'draft')])

    def test_denials_preserve_storage(self):
        for role, invoice_id in (('viewer', 1), ('unknown', 1),
                                 ('approver', 99), ('approver', 2), ('approver', 3)):
            with self.subTest(role=role, invoice_id=invoice_id):
                before = self.rows()
                self.assertIs(approve(self.db, role, invoice_id), False)
                self.assertEqual(self.rows(), before)
                self.assertEqual(self.db.execute(
                    'SELECT id, status FROM invoices ORDER BY id').fetchall(), before)


class SaveTests(unittest.TestCase):
    def test_results_preserve_input_and_unrelated_fields(self):
        for succeeded in (False, True):
            with self.subTest(succeeded=succeeded):
                state = dict(saved='old', draft='new', saving=True,
                             error='previous error', extra={'keep': [1]})
                before = copy.deepcopy(state)
                result = finish_save(state, succeeded)
                self.assertEqual(result, dict(
                    saved='new' if succeeded else 'old', draft='new', saving=False,
                    error=None if succeeded else 'Save failed', extra={'keep': [1]}))
                self.assertEqual(state, before)
                self.assertIsNot(result, state)


class ColorTests(unittest.TestCase):
    def test_exact_allowed_values(self):
        for value in ('var(--color-text)', 'var(--color-surface)', 'var(--color-danger)'):
            with self.subTest(value=value):
                self.assertIs(valid_color(value), True)

    def test_rejects_other_values(self):
        for value in ('var(--anything)', 'var(--other-text)', '#fff', 'red',
                      'rgb(0, 0, 0)', '', 'var(--color-text', 'var(--color-text))',
                      'var(--color-text, red)', 'var(--color-text) trailing',
                      ' var(--color-text)', 'var(--color-text)\n',
                      'var( --color-text)', 'VAR(--color-text)'):
            with self.subTest(value=value):
                self.assertIs(valid_color(value), False)


if __name__ == '__main__':
    unittest.main()

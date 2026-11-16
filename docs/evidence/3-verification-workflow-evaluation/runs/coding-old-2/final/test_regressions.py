import copy
import sqlite3
import unittest

from app import approve, delivery_fee, finish_save, valid_color


class DeliveryTests(unittest.TestCase):
    def test_free_delivery_boundary(self):
        for cents, expected in ((0, 500), (4999, 500), (5000, 0), (5001, 0)):
            with self.subTest(cents=cents):
                self.assertEqual(delivery_fee(cents), expected)


class ApprovalTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.addCleanup(self.db.close)
        self.db.execute('CREATE TABLE invoices(id INTEGER PRIMARY KEY, status TEXT)')
        self.db.executemany('INSERT INTO invoices VALUES (?, ?)',
                            ((1, 'pending'), (2, 'approved'), (3, 'draft')))
        self.db.commit()

    def rows(self):
        return self.db.execute('SELECT id, status FROM invoices ORDER BY id').fetchall()

    def test_approver_persists_pending_approval(self):
        self.assertIs(approve(self.db, 'approver', 1), True)
        self.assertEqual(self.rows(), [(1, 'approved'), (2, 'approved'), (3, 'draft')])
        self.db.rollback()
        self.assertEqual(self.rows(), [(1, 'approved'), (2, 'approved'), (3, 'draft')])

    def test_rejected_requests_leave_storage_unchanged(self):
        for role, invoice_id in (('viewer', 1), ('unknown', 1), ('approver', 99),
                                 ('approver', 2), ('approver', 3)):
            with self.subTest(role=role, invoice_id=invoice_id):
                before = self.rows()
                self.assertIs(approve(self.db, role, invoice_id), False)
                self.assertEqual(self.rows(), before)


class SaveTests(unittest.TestCase):
    def test_save_results_preserve_input_and_unrelated_fields(self):
        for succeeded in (False, True):
            with self.subTest(succeeded=succeeded):
                state = dict(saved='old', draft='edited', saving=True,
                             error='Previous error', invoice_id=42)
                before = copy.deepcopy(state)
                result = finish_save(state, succeeded)
                self.assertEqual(result, dict(saved='edited' if succeeded else 'old',
                                              draft='edited', saving=False,
                                              error=None if succeeded else 'Save failed',
                                              invoice_id=42))
                self.assertEqual(state, before)
                self.assertIsNot(result, state)


class ColorTests(unittest.TestCase):
    def test_exact_allowed_values(self):
        for value in ('var(--color-text)', 'var(--color-surface)', 'var(--color-danger)'):
            with self.subTest(value=value):
                self.assertTrue(valid_color(value))

    def test_other_values_are_rejected(self):
        for value in ('var(--other)', '#fff', 'red', '', 'var(--color-text',
                      'var(--color-text))', 'var(--color-text, red)',
                      ' var(--color-text)', 'var(--color-text) ', 'var( --color-text)',
                      'VAR(--color-text)', 'var(--color-text);'):
            with self.subTest(value=value):
                self.assertFalse(valid_color(value))

import unittest
from app import delivery_fee, valid_color


class Existing(unittest.TestCase):
    def test_delivery(self):
        self.assertEqual(delivery_fee(100), 500)
        self.assertEqual(delivery_fee(6000), 0)

    def test_color(self):
        self.assertTrue(valid_color("var(--color-text)"))
        self.assertFalse(valid_color("#fff"))


if __name__ == "__main__":
    unittest.main()

# test register.py

import unittest

from cash_register import register, NegativePriceError


class TestRegister(unittest.TestCase):
    def setUp(self):
        """Set up test class under test."""
        self.cash_register = register.CashRegister()
        self.cash_register.scan_item("SKU001", 13.5)
        self.cash_register.scan_item("SKU002", 100, 20)
        self.cash_register.scan_item("SKU003", 234.65, 2)

    def test_running_total(self):
        """Return running total."""
        # assert
        self.assertEqual(self.cash_register.total(), 2482.8)

    def test_reset(self):
        """Return reset cash register."""
        # act
        self.cash_register.reset()
        self.total_items = len(self.cash_register.items)

        # assert
        self.assertEqual(self.cash_register.total(), 0)
        self.assertEqual(self.total_items, 0)

    def test_negative_price(self):
        """Return negative price."""
        # arrange
        item_sku = "SKU004"
        item_price = -100.50

        # assert
        self.assertRaises(NegativePriceError, self.cash_register.scan_item, item_sku, item_price)

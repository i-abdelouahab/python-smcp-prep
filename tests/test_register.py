# test register.py

import unittest
from decimal import Decimal

from cash_register.exceptions import DiscountError, NegativePriceError
from cash_register.register import CashRegister


class TestRegister(unittest.TestCase):
    def setUp(self):
        """Set up test class under test."""
        self.cash_register = CashRegister()
        self.cash_register.scan_item("SKU001", 13.5)
        self.cash_register.scan_item("SKU002", 100, 20)
        self.cash_register.scan_item("SKU003", 234.65, 2)

    def test_running_total(self):
        """Return running total."""
        # assert
        self.assertEqual(self.cash_register.total(), Decimal("2482.80"))

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
        self.assertRaises(
            NegativePriceError, self.cash_register.scan_item, item_sku, item_price
        )

    def test_total_with_discount_10_percent(self):
        """Return total with discount."""
        # act
        self.cash_register.apply_discount(12)

        # assert
        self.assertLess(self.cash_register.total(), Decimal("2482.80"))
        self.assertEqual(self.cash_register.total(), Decimal("2184.86"))

    def test_total_after_discount_removal(self):
        """Return total after discount removal."""
        # arrange and verify discounted total
        self.cash_register.apply_discount(12)
        self.assertLess(self.cash_register.total(), Decimal("2482.80"))

        # act
        self.cash_register.remove_discount()

        # assert
        self.assertEqual(self.cash_register.total(), Decimal("2482.80"))

    def test_invalid_discount(self):
        """Return invalid discount."""
        # arrange
        discount = -10

        # assert
        self.assertRaises(DiscountError, self.cash_register.apply_discount, discount)

    def test_receipt_accuracy(self):
        """Return correct receipt with discount."""
        # act
        self.cash_register.apply_discount(Decimal("12"))
        receipt = self.cash_register.to_receipt()

        # assert receipt
        self.assertEqual(receipt.total_brut, Decimal("2482.80"))
        self.assertEqual(receipt.discount_pct, Decimal("12"))
        self.assertEqual(receipt.total_due, Decimal("2184.86"))
        self.assertEqual(len(receipt.items), 3)

        # assert an item
        item = receipt.items[0]
        self.assertEqual(item.sku, "SKU001")
        self.assertEqual(item.qty, 1)
        self.assertEqual(item.unit_price, Decimal("13.5"))

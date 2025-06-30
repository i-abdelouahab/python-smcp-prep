from decimal import Decimal

from cash_register.exceptions import DiscountError, NegativePriceError
from cash_register.models import LineItem, Receipt


class CashRegister:
    """Basic cash register for SMCP store."""

    def __init__(self, discount: Decimal = Decimal("0.0")):
        self.discount = discount
        self.items: list[LineItem] = []

    def scan_item(self, sku: str, price: Decimal, quantity: int = 1) -> None:
        """Scan and add an item to the cash register list."""
        if price <= 0:
            raise NegativePriceError(price)

        item = LineItem(sku=sku, unit_price=price, qty=quantity)
        self.items.append(item)

    def total(self) -> Decimal:
        """Calculate total after discount."""
        total = Decimal(sum((item.unit_price * item.qty for item in self.items)))

        if self.discount > 0:
            total = Decimal(total * (100 - self.discount) / 100)

        return total.quantize(Decimal("0.01"))

    def reset(self) -> None:
        """Reset the cash register."""
        self.items.clear()
        self.discount = Decimal("0.0")

    def apply_discount(self, percent: Decimal) -> None:
        """Apply discount to the total."""
        if percent <= 0 or percent >= 100:
            raise DiscountError(percent)
        self.discount = percent

    def remove_discount(self) -> None:
        """Remove any discount."""
        self.discount = Decimal("0.0")

    def to_receipt(self) -> Receipt:
        """Generate a Receipt dataclass with details."""
        total_brut = Decimal(sum(item.unit_price * item.qty for item in self.items))
        total_due = self.total()

        return Receipt(
            items=self.items.copy(),
            total_brut=total_brut.quantize(Decimal("0.01")),
            discount_pct=self.discount,
            total_due=total_due,
        )

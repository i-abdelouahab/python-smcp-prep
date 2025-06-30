from dataclasses import dataclass
from decimal import Decimal


@dataclass
class LineItem:
    sku: str
    qty: int
    unit_price: Decimal


@dataclass
class Receipt:
    items: list[LineItem]
    total_brut: Decimal
    discount_pct: Decimal
    total_due: Decimal

from .exceptions import NegativePriceError

class CashRegister:
    """Basic cash register for SMCP store."""

    def __init__(self):
        """Initialize the list of items."""
        self.items = []

    def scan_item(self, sku: str, price: float, quantity: int = 1) :
        """
        Scan and add an item to the cash register list.

        :param sku: sku of the item.
        :param price: price of the item.
        :param quantity: quantity of the item.
        :return: cash register.
        """
        if price < 0 :
            raise NegativePriceError(price)
        else :
            item = dict()
            item["sku"] = sku
            item["price"] = price
            item["quantity"] = quantity
            self.items.append(item)

    def total(self) -> float:
        """
        Calculate the total cash register.

        :return:
        """
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]

        return total

    def reset(self):
        """Reset the cash register."""
        self.items.clear()

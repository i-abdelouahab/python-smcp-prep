from cash_register.exceptions import NegativePriceError, DiscountError


class CashRegister:
    """Basic cash register for SMCP store."""

    def __init__(self, discount = 0.0):
        """Initialize the list of items."""
        self.discount = discount
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
            item["discounted_price"] = price
            item["price"] = price
            item["quantity"] = quantity
            self.items.append(item)

    def total(self) -> float:
        """
        Calculate the total cash register.

        :return: (float) total cash register.
        """
        total = 0
        for item in self.items:
            if self.discount > 0.0 :
                total += item["discounted_price"] * item["quantity"]
            else:
                total += item["price"] * item["quantity"]

        return total

    def reset(self):
        """Reset the cash register."""
        self.items.clear()

    def apply_discount(self, percent: float):
        """Apply discount to the cash register."""
        if percent < 0 or percent > 100 :
            raise DiscountError(percent)
        else :
            self.discount = percent

        for item in self.items :
            item["discounted_price"] = item["price"] * (100 - self.discount) / 100


    def remove_discount(self):
        """Remove discount from the cash register."""
        self.discount = 0.0
        for item in self.items :
            item["discounted_price"] = item["price"]

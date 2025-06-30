"""Contains all the exceptions raised by this module."""

class NegativePriceError(Exception):
    """Raised when a negative price is encountered."""
    def __init__(self, price, message="Negative price is encountered."):
        """Initialize the exception."""
        self.price = price
        self.message = message

    def __str__(self):
        """Return string representation of the exception."""
        return f'{self.message}  Price : {self.price}'


class DiscountError(Exception):
    """Raised when a discount is encountered."""
    def __init__(self, discount, message="Invqlid dicount."):
        """Initialize the exception."""
        self.discount = discount
        self.message = message

    def __str__(self):
        """Return string representation of the exception."""
        return f'{self.message}  Discount : {self.discount}'
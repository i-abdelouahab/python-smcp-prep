"""Contains all the exceptions raised by this module."""

from decimal import Decimal


class NegativePriceError(Exception):
    """Raised when a negative price is encountered."""

    def __init__(
        self, price: Decimal, message: str = "Negative price is encountered."
    ) -> None:
        """Initialize the exception."""
        self.price = price
        self.message = message

    def __str__(self) -> str:
        """Return string representation of the exception."""
        return f"{self.message}  Price : {self.price}"


class DiscountError(Exception):
    """Raised when a discount is encountered."""

    def __init__(self, discount: Decimal, message: str = "Invalid discount."):
        """Initialize the exception."""
        self.discount = discount
        self.message = message

    def __str__(self) -> str:
        """Return string representation of the exception."""
        return f"{self.message}  Discount : {self.discount}"

"""Contains all the exceptions raised by this module."""

class NegativePriceError(Exception):
    """Raised when a negative price is encountered."""
    def __init__(self, price, message="Negative price is encountered."):
        """Initialize the exception."""
        self.price = price
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """Return string representation of the exception."""
        return f'{self.message}  Price : {self.price}'
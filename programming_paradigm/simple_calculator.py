class SimpleCalculator:
    """A simple calculator class for basic arithmetic operations."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the result of subtracting b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the result of dividing a by b. Raise error if b is 0."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

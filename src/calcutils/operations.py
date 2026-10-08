"""Small reusable mathematical utility functions."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def average(numbers: list) -> float:
    """Return the arithmetic mean, or 0.0 for an empty list."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

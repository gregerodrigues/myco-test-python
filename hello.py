"""A minimal greeting module."""


def greet(name: str = "world") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name.strip() or 'world'}!"


def average(values: list[int]) -> float:
    """Return the average of a list of values."""
    return sum(values) / len(values)


if __name__ == "__main__":
    print(greet("Ada"))
"""A minimal greeting module."""


def greet(name: str = "world") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name.strip() or 'world'}!"


if __name__ == "__main__":
    print(greet("Ada"))

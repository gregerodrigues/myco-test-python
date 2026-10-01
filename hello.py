"""A minimal greeting module."""


def greet(name: str = "world") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name.strip() or 'world'}!"


if __name__ == "__main__":
    print(greet("Ada"))

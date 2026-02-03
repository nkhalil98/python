import doctest


def add(a, b):
    """
    Adds two numbers.

    >>> add(1, 2)
    3

    >>> add(2, 3)
    5
    """
    return a + b


if __name__ == "__main__":
    doctest.run_docstring_examples(add, globals(), name=add.__name__)

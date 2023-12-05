#!/usr/bin/python3
"""checks if it is instance of class and inheritance"""


def is_kind_of_class(obj, a_class):
    """kind of class through inheritance or anything

    Args:
        obj: object to check
        a_class: class to check from

    Returns:
        True if and false else
    """
    return (isinstance(obj, a_class))

#!/usr/bin/python3
def add_inteer(a, b=98):
    """Return the integer addition of a and b
    Raise: TypeError
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer"):
            if not isinstance(b, (int, float)):
                raise TypeError("b must be an integer")
            return int(a) + int(b)

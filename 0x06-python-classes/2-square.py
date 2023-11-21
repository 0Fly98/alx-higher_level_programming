#!/usr/bin/python3
def __init__(self, size=0):
    if not isinstance(size, int):

        raise
    TypeError("size must be an intger")
elif size < 0:
    raise
ValueError("ize must be >= 0")
else:
    self._size = size

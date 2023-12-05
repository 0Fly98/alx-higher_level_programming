#!/usr/bin/python3
"""a base geometry class"""


class BaseGeometry:
    """a base geometry class"""

    def area(self):
        """It raises an exception for area not def"""
        raise Exception("area() is not implemented")

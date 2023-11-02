#!/usr/bin/python3
if _name_ == "_main_:
    from calculator_1 import add, sub, mul, div

    operations = {
    'addition': add,
    'subtraction': sub,
    'multiplication': mul,
    'division': div
    }

    a = 10
    b = 5

    for operation, function in operations.items():
    print("The result of the {} of {:d} and {:d} is {:d}" .format(operation, a, b, function(a, b)))

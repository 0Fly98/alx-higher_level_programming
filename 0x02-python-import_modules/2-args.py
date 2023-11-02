#!/usr/bin/python3
import sys
import argparse

parser = argparse.ArgumentParser(description="Prints the number of and the list of its arguments")
parser.add_argument("args", nargs="*", help="The arguments to print")
arguments = parser.parse_args()

size = len(arguments.args)

if size > 1:
    print(f"{size} arguments:")
    for i, arg in enumerate(arguments.args, start=1):
        print(f"{i}: {arg}")

elif size == 0:
    print(f"{size} arguments.")
    sys.exit()

else:
    print(f"{size} argument:")
    print(f"{size}: {arguments.args[0]}")

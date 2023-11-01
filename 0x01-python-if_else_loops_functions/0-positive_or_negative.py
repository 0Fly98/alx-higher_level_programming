#!/usr/bin/python3
import random

number = random.randint(-10, 10)
signs = {1: "positive", 0: "zero", -1: "negative"}

print(f"{number:d} is {signs[number//abs(number) if number else 0]}")

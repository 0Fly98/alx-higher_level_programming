#!/usr/bin/python3
import random
number = random.randint(-10, 10)
descriptions = {
    number > 0: f"{number:d} is positive",
    number == 0: f"{number:d} is zero",
    number < 0: f"{number:d} is negative"
}
print(descriptions[True])

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10 * (-1 if number < 0 else 1)

message = "Last digit of " + str(number) + " is " + str(last_digit) + " and is"
if last_digit == 0:
    print(message, "0")
elif last_digit > 5:
    print(message, "greater than 5")
elif last_digit < 6 and not 0:
    print(message, "less than 6 and not 0")

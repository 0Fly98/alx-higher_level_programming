#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Define a dictionary to map number ranges to their descriptions
descriptions = {
    number > 0: "{} is positive".format(number),
    number == 0: "{} is zero".format(number),
    number < 0: "{} is negative".format(number)
}

# Print the description for the number
print(descriptions[True])

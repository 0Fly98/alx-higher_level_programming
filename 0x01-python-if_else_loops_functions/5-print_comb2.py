#!/usr/bin/python3

for u in range(100):
    if u == 99:
        print(99)
    else:
        print("{:02d}, ".format(u), end='')

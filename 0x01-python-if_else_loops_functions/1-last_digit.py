#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ladi = abs(number) % 10
if number < 0:
    ladi = -ladi
if ladi > 5:
    print(f"Last digit of {number:d} is {ladi:d} and is greater than 5")
elif ladi == 0:
    print(f"Last digit of {number:d} is {ladi:d} and is 0")
else:
    print(f"Last digit of {number:d} is {ladi:d} and is less than 6 and not 0")

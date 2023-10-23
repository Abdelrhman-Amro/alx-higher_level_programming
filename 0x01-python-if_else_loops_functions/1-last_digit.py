#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

n = abs(number) % 10
if number < 0: 
    n = n * -1
print("Last digit of {} is {} and is".format(number, n), end=" ")
if n == 0:
    print("0")
elif n > 5:
    print("greater than 5")
else:
    print("less than 6")

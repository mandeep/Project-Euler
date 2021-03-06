"""
Project: Project Euler - Problem 43: Sub-string Divisibility
Author: Mandeep Bhutani
Date: 4/18/2015

Problem: The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the
digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
d2d3d4=406 is divisible by 2, d3d4d5=063 is divisible by 3, d4d5d6=635 is divisible by 5,
d5d6d7=357 is divisible by 7, d6d7d8=572 is divisible by 11, d7d8d9=728 is divisible by 13,
d8d9d10=289 is divisible by 17. Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations

result = 0
primes = [2, 3, 5, 7, 11, 13, 17]

for x in permutations(str(1234567890)):
    total = []
    y = "".join(x)
    for i in range(1, 8):
        divisors = int(y[i] + y[i+1] + y[i+2])
        if divisors % primes[i-1] == 0:
            total.append(True)
    if all(total) is True and len(total) == 7:
        result += int("".join(x))
print(result)

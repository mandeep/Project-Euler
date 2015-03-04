"""
Title: Project Euler - Problem 10: Summation of Primes
Author: Mandeep Bhutani
Date: 2/24/2015

Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

References: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes;
https://docs.python.org/2/library/stdtypes.html
"""
from math import sqrt


def is_prime(n):
    for x in range(2, int(sqrt(n) + 1)):
        if n % x == 0:
            return False
    else:
        return True


def summation(s):
    result = []
    p = 1
    while p < s:
        p += 1
        if is_prime(p) == True:
            result.append(p)
    return sum(result)
print summation(2000000)

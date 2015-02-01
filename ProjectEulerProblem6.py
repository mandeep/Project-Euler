"""
Project: Project Euler - Problem 6: Sum Square Difference
Author: Mandeep Bhutani
Date: 1/30/2015

Problem:
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
print sum([x for x in range(101)])**2 - sum([x ** 2 for x in range(101)])
# Using the sum() function as well as list comprehension to enhance readability.
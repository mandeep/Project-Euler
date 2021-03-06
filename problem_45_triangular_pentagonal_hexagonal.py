"""
Project: Project Euler - Problem 45: Triangular, Pentagonal, Hexagonal
Author: Mandeep Bhutani
Date: 3/31/2015

Problem: Triangle, pentagonal, and hexagonal numbers are generated by the
following formulae: n(n+1)/2, n(3n-1)/2, n(2n-1). It can be verified that
T285 = P165 = H143 = 40755. Find the next triangle number that is also
pentagonal and hexagonal.

Description: Because all hexagonal numbers are triangle numbers, it is only
necessary to check the equality between hexagonal and pentagonal numbers.
While this shortens the processing time of the problem, it is still a naive
solution in that it takes 135s to complete.
"""

pentagon = [n * (3 * n - 1) / 2 for n in xrange(1, 100000)]
hexagon = [n * (2 * n - 1) for n in xrange(1, 100000)]
for i in hexagon:
    if i in pentagon and i > 40755:
        print i
        break

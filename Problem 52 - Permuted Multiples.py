"""
Project: Project Euler - Problem 52: Permuted Multiples
Author: Mandeep Bhutani
Date: 4/4/2015

Problem: It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order. Find the smallest
positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
x = 125874
while True:
    x += 1
    if sorted(set(str(x))) == sorted(set(str(x * 2))) == \
        sorted(set(str(x * 3))) == sorted(set(str(x * 4))) == \
            sorted(set(str(x * 5))) == sorted(set(str(x * 6))):
        print x
        break

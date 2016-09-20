/*
Project: Project Euler - Problem 9: Special Pythagorean Triplet
Author: Mandeep Bhutani
Date: 09/19/2016

Problem: A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 + 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product of a*b*c.
*/
#include <iostream>

int main() {
    for (int a = 1; a < 1000; a++) {
        for (int b = 1; b < 1000 - a; b++) {
            int c = 1000 - a - b;
            if ((a * a) + (b * b) == (c * c)) {
                int result = a * b * c;
                std::cout << result << std::endl;
            }
        }
    }
}
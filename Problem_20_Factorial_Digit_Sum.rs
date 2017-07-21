/*
Project: Project Euler - Problem 20: Factorial Digit Sum
Author: Mandeep Bhutani
Date: 10/25/2016

Problem: n! means n * (n-1) * ... * 3 * 2 * 1
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
*/
extern crate num;

use num::Integer;
use num::BigUint;
use num::traits::{One, ToPrimitive, Zero};


fn factorial(n: usize) -> BigUint {
    (1..n+1).fold(One::one(), |acc, x| acc * BigUint::from(x))
}


fn sum_digits(mut num: BigUint) -> u32 {
    let mut summation = 0;
    while num > Zero::zero() {
        let digit = Integer::mod_floor(&num, &BigUint::from(10 as u32));
        num = Integer::div_floor(&num, &BigUint::from(10 as u32));
        summation += ToPrimitive::to_u32(&digit).unwrap();
    }
    summation
}


fn main() {
    println!("{}", sum_digits(factorial(100)));
}
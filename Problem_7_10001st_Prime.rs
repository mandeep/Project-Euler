/*
Title: Project Euler - Problem 7: 10001st Prime
Author: Mandeep Bhutani
Date: 10/21/2016

Problem: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13. What is the 10,001st prime number?
*/
fn is_prime(n: i32) -> bool {
    if n < 2 { return false; }
    let temp: f64 = n as f64;
    let limit: i32 = temp.sqrt() as i32;
    for i in 2..limit+1 { if n % i == 0 { return false; } }
    true
}

fn main() {
    let mut count = 0;
    let mut number = 1;
    while count < 10001 { 
        number += 1;
        if is_prime(number) { count += 1; } }
    println!("{}", number);
}
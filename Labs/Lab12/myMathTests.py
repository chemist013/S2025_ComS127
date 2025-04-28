# Joshua Hamaker        04/11/2025
# Lab 11 - Unit Tests for myMath

import math
import myMath


def test_add():
    assert myMath.add(1, 1) == 2
    assert myMath.add(-1, -1) == -2
    assert myMath.add(0.5, 1) == 1.5


def test_subtract():
    assert myMath.subtract(1, 1) == 0
    assert myMath.subtract(-1, -1) == 0
    assert myMath.subtract(0.5, 1) == -0.5


def test_multiply():
    assert myMath.multiply(1, 5) == 5
    assert myMath.multiply(-5, 1) == -5
    assert myMath.multiply(0, 1) == 0
    assert myMath.multiply(0.5, 20) == 10


def test_divide():
    assert myMath.divide(5, 1) == 5
    assert myMath.divide(-5, 1) == -5
    assert myMath.divide(0, 1) == 0
    assert myMath.divide(20, 0.5) == 40


def test_power():
    assert myMath.power(5, 0) == 1
    assert myMath.power(5, 2) == 25
    assert myMath.power(5, -1) == 0.2


def test_factorial():
    assert myMath.factorial(0) == myMath.factorial(1) == 1
    assert myMath.factorial(4) == 24
    # assert myMath.factorial(-1) == ValueError

def test_is_prime():
    assert myMath.is_prime(13) == True
    assert myMath.is_prime(25) == False


def test_sum_of_digits():
    assert myMath.sum_of_digits(123) == 6
    assert myMath.sum_of_digits(-123) == 6
    assert myMath.sum_of_digits(1.23) == 6
    

def test_gcd():
    assert myMath.gcd(20, 25) == 5
    assert myMath.gcd(20, 100) == 20
    assert myMath.gcd(100, 0) == math.gcd(100, 0)
    assert myMath.gcd(100, -1) == math.gcd(100, -1)


def test_fib():
    assert myMath.fib(0) == 0
    assert myMath.fib(1) == 1
    assert myMath.fib(2) == 1
    assert myMath.fib(3) == 2
    assert myMath.fib(7) == 13


def test_lcm():
    assert myMath.lcm(20, 25) == 100
    assert myMath.lcm(20, 100) == 100
    assert myMath.lcm(100, 0) == math.lcm(100, 0)
    assert myMath.lcm(100, -1) == math.lcm(100, -1)


def test_square_root():
    assert myMath.square_root(0) == 0
    assert myMath.square_root(4) == 2
    assert myMath.square_root(169) == 13


def test_abs_diff():
    assert myMath.abs_diff(-1, 1) == 2
    assert myMath.abs_diff(-55, 1) == 56
    assert myMath.abs_diff(55, 1) == 54


def test_log():
    assert myMath.log(1) == 0
    assert round(myMath.log(100), 3) == 2
    assert myMath.log(256, 2) == 8


def test_mod():
    assert myMath.mod(67, 11) == 1
    assert myMath.mod(67, 67) == 0
    assert myMath.mod(103, 100) == 3


def test_mean():
    assert myMath.mean([1, 2, 3]) == 2
    assert myMath.mean([1, 2, 3, 4]) == 2.5
    assert myMath.mean([1, 2, 3, 4, 5]) == 3


def test_median():
    assert myMath.median([1, 2, 3]) == 2
    assert myMath.median([1, 2, 3, 4]) == 2.5
    assert myMath.median([1, 2, 3, 4, 5]) == 3


def test_mode():
    assert myMath.mode([1, 2, 3, 4, 5]) == 1
    assert myMath.mode([1, 2, 3, 4, 5, 5]) == 5
    assert myMath.mode([1, 2, 3, 4, 5, 5, 6]) == 5


def test_celsius_to_fahrenheit():
    assert myMath.celsius_to_fahrenheit(0) == 32
    assert myMath.celsius_to_fahrenheit(100) == 212
    assert myMath.celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    assert myMath.fahrenheit_to_celsius(32) == 0
    assert myMath.fahrenheit_to_celsius(212) == 100
    assert myMath.fahrenheit_to_celsius(-40) == -40


def test_inverse():
    assert myMath.inverse(1) == 1
    assert myMath.inverse(-1) == -1
    assert myMath.inverse(0.5) == 2


def test_triangular_number():
    assert myMath.triangular_number(0) == 0
    assert myMath.triangular_number(1) == 1
    assert myMath.triangular_number(2) == 3
    assert myMath.triangular_number(3) == 6
    assert myMath.triangular_number(4) == 10
# Joshua Hamaker      02/21/2025
# Lab05 - Finance Functions

# This is a module that contains the functions annualPercentageRate() and
# compoundAmount() from Lab 04. These are to be called by calculationTest.py

def annualPercentageRate(i: float, f: float, a: float, d: float) -> float:
    # formula taken from https://www.investopedia.com/terms/a/apr.asp
    apr = (((i + f) / a) / d) * 100
    return apr

def compoundAmount(p: float, r: float, n: float, t:float) -> float:
    # formula taken from https://en.wikipedia.org/wiki/Compound_interest#Calculation
    a = p * (1 + (r/100) / n)**(n * t)
    return a
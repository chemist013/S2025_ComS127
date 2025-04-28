# Joshua Hamaker      02/21/2025
# Lab05 - Ohm's Law Functions

# This is a module that contains the functions calculateCurrent(), calculateResistance() and
# calculateVoltage() from Lab 04. These are to be called by calculationTest.py

def calculateCurrent(v: float, r: float) -> float:
    # formula taken from https://en.wikipedia.org/wiki/Ohm%27s_law
    i = v/r
    return i

def calculateResistance(v: float, i: float) -> float:
    # formula taken from https://en.wikipedia.org/wiki/Ohm%27s_law
    r = v/i
    return r

def calculateVoltage(i: float, r: float) -> float:
    # formula taken from https://en.wikipedia.org/wiki/Ohm%27s_law
    v = i*r
    return v
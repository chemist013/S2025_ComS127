# Joshua Hamaker      02/21/2025
# Lab05 - Shape Functions

# This is a module that contains the functions areaOfRectangle(), rectanglePerimeter(), 
# areaOfCircle(), and circleCircumference() from Lab 04. These are to be called by calculationTest.py

import math

def areaOfRectangle(b: float, h: float) -> float:
    # formula taken from https://en.wikipedia.org/wiki/Rectangle#Formulae
    A = b*h
    return A

def rectanglePerimeter(b: float, h: float) -> float:
    # formula taken from https://en.wikipedia.org/wiki/Rectangle#Formulae
    P = 2*(b+h)
    return P

def areaOfCircle(r: float) -> float:
    # formula taken from https://en.wikipedia.org/wiki/Circle#Area_enclosed
    A = math.pi*(r**2)
    return A

def circleCircumference(r: float) -> float:
    # formula taken from https://en.wikipedia.org/wiki/Circle#Circumference
    C = 2*math.pi*r
    return C
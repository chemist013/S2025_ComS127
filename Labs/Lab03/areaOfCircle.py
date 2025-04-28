# Joshua Hamaker      02/07/2025
# Lab 03 - Area of a Circle
import math

print(f"This program calculates the area of a circle")
radius = float(input(f"What should the radius of the circle be? "))
area = math.pi*(radius**2)
# formula taken from https://en.wikipedia.org/wiki/Circle#Area_enclosed

print(f"The area of your circle is {area}!")
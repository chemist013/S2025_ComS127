# Joshua Hamaker      02/07/2025
# Lab 03 - Circumference of a Circle
import math

print(f"This program calculates the circumference of a circle")
radius = float(input(f"What should the radius of the circle be? "))
circumference = 2*math.pi*radius
# formula taken from https://en.wikipedia.org/wiki/Circle#Circumference

print(f"The circumference of your circle is {circumference}!")
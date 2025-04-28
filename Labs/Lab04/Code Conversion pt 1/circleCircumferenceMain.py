# Joshua Hamaker      02/15/2025
# Lab 04 - Circumference of a Circle w/ def main()
import math

def main():
    print(f"This program calculates the circumference of a circle")
    radius = float(input(f"What should the radius of the circle be? "))
    ans = circleCircumference(radius)
    print(f"The circumference of your circle is {ans}!")

def circleCircumference(r):
    # formula taken from https://en.wikipedia.org/wiki/Circle#Circumference
    c = 2*math.pi*r
    return c

if __name__ == "__main__":
    main()
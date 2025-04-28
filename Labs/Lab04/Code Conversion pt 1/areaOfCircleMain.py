# Joshua Hamaker      02/15/2025
# Lab 04 - Area of a Circle w/ def main()
import math

def main():
    print(f"This program calculates the area of a circle")
    radius = float(input(f"What should the radius of the circle be? "))
    ans = areaOfCircle(radius)
    print(f"The area of your circle is {ans}!")

def areaOfCircle(r):
    # formula taken from https://en.wikipedia.org/wiki/Circle#Area_enclosed
    A = math.pi*(r**2)
    return A

if __name__ == "__main__":
    main()
# Joshua Hamaker      02/15/2025
# Lab 04 - Area of a Rectangle w/ def main()

def main():
    print(f"This program calculates the area of a rectangle")
    base = float(input(f"What should the base of the rectangle be? "))
    height = float(input(f"What should the height of the rectangle be? "))
    ans = areaOfRectangle(base, height)
    print(f"The area of your rectangle is {ans}!")

def areaOfRectangle(b,h):
    # formula taken from https://en.wikipedia.org/wiki/Rectangle#Formulae
    A = b*h
    return A

if __name__ == "__main__":
    main()
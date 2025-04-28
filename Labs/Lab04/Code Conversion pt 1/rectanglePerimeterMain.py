# Joshua Hamaker      02/15/2025
# Lab 04 - Perimeter of a Rectangle w/ def main()

def main():
    print(f"This program calculates the perimeter of a rectangle")
    base = float(input(f"What should the base of the rectangle be? "))
    height = float(input(f"What should the height of the rectangle be? "))
    ans = rectanglePerimeter(base, height)
    print(f"The perimeter of your rectangle is {ans}!")

def rectanglePerimeter(b,h):
    # formula taken from https://en.wikipedia.org/wiki/Rectangle#Formulae
    p = 2*(b+h)
    return p

if __name__ == "__main__":
    main()
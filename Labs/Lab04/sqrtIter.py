# Joshua Hamaker        02/14/2025
# Lab 04 - Iterative Square Root
# This program approximates the square root of a given number
# with precision (# of iterations) defined by the user

def main():
    num = float(input(f"What number do you want to take the square root of? "))
    repeats = int(input(f"How many times do you want to repeat the calculation? (higher # = more precision) "))
    print(f"Your approximated square root is:")
    print(sqrtIter(num, repeats))

def sqrtIter(x, iterations):
    # CITATION - URL: https://www.cuemath.com/algebra/square-root-of-2/
    # CITATION - Author: unknown
    # CITATION - Date Written: unknown
    # CITATION - Date Accessed: 14 Feb 2025
    y = 1
    for i in range(0, iterations):
        y = float(((x/y)+y)/2)
    return y

if __name__ == "__main__":
    main()
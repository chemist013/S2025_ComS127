# Joshua Hamaker      02/14/2025
# Lab 04 - Random Product
# This program calculates a number of random products
# in a user defined range

import random

def main():
    qty = int(input("How many random products do you want? "))
    lowerBound = int(input("What is your lower bound? "))
    upperBound = int(input("What is your upper bound (inclusive)? "))
    print("Your random product is:")
    print(randomProduct(qty, lowerBound, upperBound))

def randomProduct(numProducts, min, max):
    total = 1
    for i in range(numProducts):
        x = random.randrange(min, max + 1)
        total = total*x
    return total

if __name__ == "__main__":
    main()
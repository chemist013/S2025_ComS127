# Joshua Hamaker        02/15/2025
# Assignment 02: Lucky Calculator

# This program offers a CLI for each of the different math operations in Python
# as well as offering to generate a 'lucky number' for the user.

import random

def header():
    print(f"Lucky Calculator!")
    print(f"Created by: Joshua Hamaker")
    print(f"for ComS 1270-2")
    print(f"")

def main():
    exitLoop = False
    while not exitLoop:
        print(f"Which operation would you like to perform?")
        print(f"[a]ddition, [s]ubrtaction, [m]ultiplication, [d]ivision,")
        print(f"[i]ntiger division, m[o]dulo, [e]xponentiation,")
        print(f"generate [l]ucky number, [q]uit")
        operation = input()
        print(f"")
        if operation == "l":
            luckyNum = genLuckyNumber()
            print(f"Your lucky number is: {luckyNum}")
            print(f"")
        elif operation != "q":
            numOne = int(input(f"Please enter a number (integers only): "))
            numTwo = int(input(f"Please enter a second number (integers only): "))
            result = calc(operation, numOne, numTwo)
            print(f"The result of your calculation is: {result}")
            print(f"")
        else:
            exitLoop = True
            print(f"Goodbye!")

def calc(op, a, b):
    match op:
        case "a":
            return a + b
        case "s":
            return a - b
        case "m":
            return a * b
        case "d":
            if b == 0:
                return "DIV BY 0 ERROR"
            else:
                return a / b
        case "i":
            if b == 0:
                return "DIV BY 0 ERROR"
            else:
                return a // b
        case "o":
            if b == 0:
                return "DIV BY 0 ERROR"
            else:
                return a % b
        case "e":
            return a ** b
        case _:
            return "INPUT ERROR"

def genLuckyNumber():
    luckySeed = "init"
    input("Please enter a number: ")
    while luckySeed != "":
        luckySeed = input("Please enter another number, or press [ENTER] to continue: ")
    return random.randint(0, 99)

if __name__ == "__main__":
    header()
    main()
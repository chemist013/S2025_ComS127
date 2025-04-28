# Joshua Hamaker        02/14/2025
# Lab 04 - Resistance of a Wire w/ def main()

from multiprocessing.connection import answer_challenge


def main():
    print(f"This program calculates the resistance of a wire")
    current = float(input(f"What is the current of the wire in amperes? "))
    voltage = float(input(f"What is the voltage of the wire in volts? "))
    ans = calculateResistance(voltage, current)
    print(f"The resistance of the wire is {ans} ohms")

def calculateResistance(v,i):
    # formula taken from https://en.wikipedia.org/wiki/Ohm%27s_law
    r = v/i
    return r

if __name__ == "__main__":
    main()
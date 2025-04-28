# Joshua Hamaker        02/15/2025
# Lab 04 - Voltage of a Wire w/ def main()

def main():
    print(f"This program calculates the voltage of a wire")
    current = float(input(f"What is the current of the wire in amperes? "))
    resistance = float(input(f"What is the resistance of the wire in ohms? "))
    ans = calculateVoltage(current, resistance)
    print(f"The voltage of the wire is {ans} volts")

def calculateVoltage(i,r):
    # formula taken from https://en.wikipedia.org/wiki/Ohm%27s_law
    v = i*r
    return v

if __name__ == "__main__":
    main()
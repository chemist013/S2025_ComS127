# Joshua Hamaker        02/15/2025
# Lab 04 - Current of a Wire w/ def main()

def main():
    print(f"This program calculates the current of a wire")
    voltage = float(input(f"What is the voltage of the wire in volts? "))
    resistance = float(input(f"What is the resistance of the wire in ohms? "))
    ans = calculateCurrent(voltage, resistance)
    print(f"The current of the wire is {ans} amperes")

def calculateCurrent(v,r):
    # formula taken from https://en.wikipedia.org/wiki/Ohm%27s_law
    i = v/r
    return i

if __name__ == "__main__":
    main()
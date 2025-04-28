# Joshua Hamaker        02/07/2025
# Lab 03 - Current of a Wire

print(f"This program calculates the current of a wire")
voltage = float(input(f"What is the voltage of the wire in volts? "))
resistance = float(input(f"What is the resistance of the wire in ohms? "))
current = voltage/resistance
# formula taken from https://en.wikipedia.org/wiki/Ohm%27s_law

print(f"The current of the wire is {current} amperes")
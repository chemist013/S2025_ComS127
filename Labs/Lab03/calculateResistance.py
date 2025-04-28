# Joshua Hamaker        02/07/2025
# Lab 03 - Resistance of a Wire

print(f"This program calculates the resistance of a wire")
current = float(input(f"What is the current of the wire in amperes? "))
voltage = float(input(f"What is the voltage of the wire in volts? "))
resistance = voltage/current
# formula taken from https://en.wikipedia.org/wiki/Ohm%27s_law

print(f"The resistance of the wire is {resistance} ohms")
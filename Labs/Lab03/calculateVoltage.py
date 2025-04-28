# Joshua Hamaker        02/07/2025
# Lab 03 - Voltage of a Wire

print(f"This program calculates the voltage of a wire")
current = float(input(f"What is the current of the wire in amperes? "))
resistance = float(input(f"What is the resistance of the wire in ohms? "))
voltage = current*resistance
# formula taken from https://en.wikipedia.org/wiki/Ohm%27s_law

print(f"The voltage of the wire is {voltage} volts")
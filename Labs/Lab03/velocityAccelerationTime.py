# Joshua Hamaker        02/07/2025
# Lab 03 - Velocity from Acceleration & Time

print(f"This program calculates the final velocity of an object")
v_initial = float(input(f"Enter the initial velocity of the object in m/s: "))
acc = float(input(f"Enter the object's acceleration in m/s/s: "))
time = float(input(f"Enter the time the object traveled in seconds: "))
v_final = v_initial + acc*time

print(f"The final velocity of  the object is {v_final} m/s!")
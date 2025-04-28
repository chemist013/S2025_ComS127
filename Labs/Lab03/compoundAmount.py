# Joshua Hamaker      02/07/2025
# Lab 03 - Compound Interest

print(f"This program calculates the total amount money you will have after a certain amount of time")
principal = float(input(f"What is the principal of the loan? " ))
rate = float(input(f"What is the interest rate of your account? (don't include '%') "))
number_compounds = float(input(f"How many times does your interest compound yearly? "))
time = float(input(f"How many years are you waiting? "))
accrued_amount = principal * (1 + (rate/100) / number_compounds)**(number_compounds * time)
# formula taken from https://en.wikipedia.org/wiki/Compound_interest#Calculation

print(f"After {time} years, you will have ${accrued_amount} in your bank account!")
# Joshua Hamaker      02/07/2025
# Lab 03 - Annual Percentage Rate

print(f"This program calculates a loan's annual percentage rate or APR")
loan_amount = float(input(f"How much is the loan? "))
days_in_term = float(input(f"What is the length of th loan in days? "))
interest_charges = float(input(f"How much interest will you be paying? "))
fees = float(input(f"How much are the fees associated with the loan? "))
apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
# formula taken from https://www.investopedia.com/terms/a/apr.asp

print(f"Your loan's APR is {apr}%!")
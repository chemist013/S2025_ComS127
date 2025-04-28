# Joshua Hamaker      02/14/2025
# Lab 04 - Annual Percentage Rate w/ def main()

def main():
    print(f"This program calculates a loan's annual percentage rate or APR")
    loan_amount = float(input(f"How much is the loan? "))
    days_in_term = float(input(f"What is the length of th loan in days? "))
    interest_charges = float(input(f"How much interest will you be paying? "))
    fees = float(input(f"How much are the fees associated with the loan? "))
    ans = annualPercentageRate(interest_charges, fees, loan_amount, days_in_term)
    print(f"Your loan's APR is {ans}%!")

def annualPercentageRate(i, f, a, d):
    # formula taken from https://www.investopedia.com/terms/a/apr.asp
    apr = (((i + f) / a) / d) * 100
    return apr

if __name__ == "__main__":
    main()
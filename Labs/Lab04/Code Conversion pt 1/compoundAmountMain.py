# Joshua Hamaker      02/15/2025
# Lab 04 - Compound Interest  w/ def main()

def main():
    print(f"This program calculates the total amount money you will have after a certain amount of time")
    principal = float(input(f"What is the principal of the loan? " ))
    rate = float(input(f"What is the interest rate of your account? (don't include '%') "))
    number_compounds = float(input(f"How many times does your interest compound yearly? "))
    time = float(input(f"How many years are you waiting? "))
    ans = compoundAmount(principal, rate, number_compounds, time)
    print(f"After {time} years, you will have ${ans} in your bank account!")

def compoundAmount(p, r, n, t):
    # formula taken from https://en.wikipedia.org/wiki/Compound_interest#Calculation
    a = p * (1 + (r/100) / n)**(n * t)
    return a

if __name__ == "__main__":
    main()
# Joshua Hamaker        02/28/2025
# Lab06 - Student Loan Amortization


def main() -> None:
    print("What is the printipal of the loan?")
    principal: float = float(input())
    print("What is the annual interest rate of the loan (as a decimal)?")
    rate: float = float(input())/100
    print("What is the length of the loan in years?")
    numPeriods: int = int(input())
    studentLoanAmortization(principal, rate, numPeriods)


def studentLoanAmortization(P: float, r: float, n: int) -> None:
    print("Period\tTotal Payment Due\tComputed Interest\tPrincipal Due\tPrincipal Balance")
    print("---------------------------------------------------------------------------------------")
    mr: float = r / 12
    nm: int = n * 12
    totalPaymentDue: float = P * ( (mr * (1 + mr) ** nm) / ( (1 + mr) ** nm - 1) )
    for i in range(nm):
        computedInterest: float = P * mr
        principalDue: float = totalPaymentDue - computedInterest
        P -= principalDue
        print(f"{i + 1}\t{totalPaymentDue:.2f}\t\t\t{computedInterest:.2f}\t\t\t{principalDue:.2f}\t\t{P:.2f}")


if __name__ == "__main__":
    main()
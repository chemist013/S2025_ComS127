# Joshua Hamaker        02/19/2024
# Lab05 - Find Leap Year

# This program will determine if a year, provided
# by the user, is a leap # year or not.

def main() -> None:
    year = int(input("Enter a year: "))
    isLeapYear = findLeapYear(year)
    if isLeapYear:
        print(f"YES, {year} is a leap year.")
    else:
        print(f"NO, {year} is not a leap year.")

def findLeapYear(year: int) -> bool:
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True

if __name__ == "__main__":
    main()
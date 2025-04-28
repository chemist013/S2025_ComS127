# Joshua Hamaker        03/28/2025
# Lab 10 - Palindrome List


def main() -> None:
    endOfList = False
    lstToCheck = []
    print("Enter a list of strings to be checked:")
    print("(When finished, enter '*' to quit)")
    while not endOfList:
        str = input()
        if str == "*":
            endOfList = True
            break
        lstToCheck.append(str)
    isPalendrome = palendromeList(lstToCheck)
    if isPalendrome:
        print("This list is a palindrome.")
    else:
        print("This list is not a palindrome.")

def palendromeList(lst: list) -> bool:
    """Checks if the list is a palindrome"""
    for i in range(len(lst) // 2):
        if lst[i] != lst[len(lst) - 1 - i]:
            return False
    return True


if __name__ == "__main__":
    main()
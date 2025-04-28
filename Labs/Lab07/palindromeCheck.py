# Joshua Hamaker        02/03/2025
# Lab07 - Check Palindrome

# This program checks if an inputed string is a palindrome in two different ways

import reverseString

def main() -> None:
    """ Main fx """
    print("Please input a string: ")
    originalStr = input()
    isPalindromeV1 = palindromeCheckV1(originalStr)
    isPalindromeV2 = palindromeCheckV2(originalStr)
    if isPalindromeV1 == True and isPalindromeV2 == True:
        print(f"{originalStr} is a palindrome")
    else:
        print(f"{originalStr} is not a palindrome")


def palindromeCheckV1(s: str) -> bool:
    outBool: bool = False
    if s == "":
        outBool = False
        return outBool
    """ Compares the string to its reversed counterpart; reversal utilizes 'reverseString' module """
    outBool = s == reverseString.reverseStringV1(s)
    return outBool


def palindromeCheckV2(s: str) -> bool:
    """ Compares the characters first & last characters, second & second last characters, etc. of a string """
    outBool: bool = False
    if s == "":
        outBool = False
        return outBool
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            outBool = True
        else:
            outBool = False
            break
    return outBool

if __name__ == "__main__":
    main()
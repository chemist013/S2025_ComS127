# Joshua Hamaker        03/04/2025
# Lab07 - Reverse String

# This file is a hub for a number of different methods to reverse strings

def main() -> None:
    """ Main fx """
    print("Please input a string that is to be reversed:")
    originalStr: str = input()
    revStr1: str = reverseStringV1(originalStr)
    revStr2: str = reverseStringV2(originalStr)
    revStr3: str = reverseStringV3(originalStr)
    revStr4: str = reverseStringV4(originalStr)
    revStr5: str = reverseStringV5(originalStr)
    print(revStr1)
    print(revStr2)
    print(revStr3)
    print(revStr4)
    print(revStr5)


def reverseStringV1(s: str) -> str:
    """ Uses string slicing to reverse a string """
    outStr: str = s[::-1]
    return outStr


def reverseStringV2(s: str) -> str:
    """ Uses the built in '.reversed()' function to reverse a string """
    outStr = "".join(reversed(s))
    return outStr


def reverseStringV3(s: str) -> str:
    """ Uses a 'for' loop w/ 'range()' to construct a string from end to beginning """
    outStr = ""
    for i in range(len(s)-1, -1, -1):
        outStr += s[i]
    return outStr


def reverseStringV4(s: str) -> str:
    """ Uses a 'for' loop to construct a string by adding each character to the beginning of the string """
    outStr: str = ""
    for i in s:
        outStr = i + outStr
    return outStr


def reverseStringV5(s: str) -> str:
    """ Uses a 'while' loop to construct a string by adding each character to the beginning of the string """
    outStr: str = ""
    i = 0
    while len(outStr) != len(s):
        outStr = s[i] + outStr
        i += 1
    return outStr


if __name__ == "__main__":
    main()
# Joshua Hamaker        03/05/2025
# Lab07 - Find Substring

# This program reports the index of the first instance of a string contained in another string

def main() -> None:
    """ Main fx """
    print("Please input a string: ")
    originalStr = input()
    print("Please input a substring: ")
    subStr = input()
    subStrIndex1 = findSubStringV1(originalStr, subStr)
    subStrIndex2 = findSubStringV2(originalStr, subStr)
    subStrIndex3 = findSubStringV3(originalStr, subStr)
    print(subStrIndex1)
    print(subStrIndex2)
    print(subStrIndex3)
    return


def findSubStringV1(s: str, sub: str) -> int:
    """ Uses the built in '.find()' string method """
    if s == "" or sub == "":
        return -1
    return s.find(sub)


def findSubStringV2(s: str, sub: str) -> int:
    """ Uses the built in '.index()' string method """
    if s == "" or sub == "":
        return -1
    if (s + sub).index(sub) == len(s):
        return -1
    else:
        return s.index(sub)


def findSubStringV3(s: str, sub: str) -> int:
    """ Iterates through each character of a sting to find a substring """
    if s == "" or sub == "":
        return -1
    for i in range(len(s)):
        if s[i:i+len(sub)] == sub:
            return i
    return -1


if __name__ == "__main__":
    main()
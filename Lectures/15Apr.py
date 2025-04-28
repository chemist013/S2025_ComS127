# Joshua Hamaker        04/15/2025
# Exam #2 review

## Question B
def transformString(s: str) -> str:
    outStr = ""
    skip = 0
    for c in range(len(s)):
        if skip > 0:
            skip -= 1
            continue
        elif c + 2 < len(s) and s[c] == s[c+1] == s[c+2]:
            outStr += "X"
            skip = 2
        elif c + 1 < len(s) and s[c] == s[c+1]:
            outStr += s[c]*3
            skip = 1
        else:
            outStr += s[c]
    return outStr



def main() -> None:
    s = input()
    ans = transformString(s)
    print(f"The answer is {ans}")


if __name__ == '__main__':
    main()
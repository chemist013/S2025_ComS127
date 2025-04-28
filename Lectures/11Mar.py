# Joshua Hamaker        03/11/2025
# Review for Exam 1


def lucasString(n: int) -> str:
    """ Returns the nth number in the Lucas sequence """
    if n < 0:
        return "ERROR"
    match n:
        case 0:
            return "2"
        case 1:
            return "2, 1"
    outStr = "2, 1"
    nMinusTwo = 2
    nMinusOne = 1
    for i in range (2, n + 1):
        outStr += ", " + str(nMinusTwo + nMinusOne)
        nMunusTwo = nMinusOne
        nMinusOne = nMinusTwo + nMinusOne
    return outStr
    

def main() -> None:
    """ Main fx """
    ansE = lucasString(4)
    print(ansE)


if __name__ == "__main__":
    main()
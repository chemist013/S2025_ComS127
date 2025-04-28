# Joshua Hamaker        04/03/2025
# Lecture notes for 04/03


def addPosIntsV1(a: int, b: int) -> int: # this way is better
    if a < 0 or b < 0:
        return -1
    return a + b


def addPosIntV2(a: int, b: int) -> int:
    if a >= 0 and b >= 0:
        return a + b
    return -1


def addPosIntV3(a: int, b: int) -> int:
    pass


def main() -> None:
    pass 


if __name__ == '__main__':
    main()
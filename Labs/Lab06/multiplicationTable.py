# Joshua Hamaker        02/28/2025
# Lab06 - Multiplication Table

def main() -> None:
    min = int(input("What number should the multiplication table start at? "))
    max = int(input("What number should the multiplication table end at? "))
    multiplicationTable(min, max)


def multiplicationTable(start: int, final: int) -> None:
    size = final - start + 2
    for i in range(1, size):
        oldStr = ""
        row = start + i - 1
        for j in range(1, size):
            currentStr = oldStr + str(row * (start + j - 1)) + '\t'
            oldStr = currentStr
        print(currentStr)


if __name__ == "__main__":
    main()
# Joshua Hamaker        03/28/2025
# Lab 10 - Find min & max

def main() -> None:
    endOfList = False
    lstToSort = []
    print("Enter an intiger to be sorted:")
    while not endOfList:
        num = input()
        if num == "*":
            endOfList = True
            break
        try:
            num = int(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        lstToSort.append(num)
        print("Enter another intiger to be sorted, or '*' to quit:")
    minValue = findMin(lstToSort)
    maxValue = findMax(lstToSort)
    print(f"The smallest value in the list is: {minValue}")
    print(f"The largest value in the list is: {maxValue}")


def findMin(lst: list) -> int:
    """Finds the smallest value in a list of ints"""
    min = lst[0]
    for i in range(1, len(lst)):
        checkVal = lst[i]
        if checkVal < min:
            min = lst[i]
    return min


def findMax(lst: list) -> int:
    """Finds the largest value in a list of ints"""
    max = lst[0]
    for i in range(1, len(lst)):
        checkVal = lst[i]
        if checkVal > max:
            max = lst[i]
    return max


if __name__ == "__main__":
    main()
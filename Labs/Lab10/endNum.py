# Joshua Hamaker        03/28/2025
# Lab 10 - endNum


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
    print("Which number should end the list?")
    validEndNum = False
    while not validEndNum:
        endingNumber = input()
        try:
            endingNumber = int(endingNumber)
            validEndNum = True
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
    sortedLst = endNum(lstToSort, endingNumber)
    print(sortedLst)


def endNum(lst: list, end: int) -> list:
    """Returns a new list wherein all occurences of 'end' are moved to the end of the list"""
    outLst = []
    for i in range(len(lst)):
        if lst[i] != end:
            outLst.append(lst[i])
    for i in range(lst.count(end)):
        outLst.append(end)
    return outLst


if __name__ == "__main__":
    main()
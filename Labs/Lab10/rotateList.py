# Joshua Hamaker        03/28/2025
# Lab 10 - Rotate List

def main() -> None:
    endOfList = False
    lstToRotate = []
    print("Enter an intiger:")
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
        lstToRotate.append(num)
        print("Enter another intiger, or '*' to quit:")
    print("How should this list be rotated?")
    validRotValue = False
    while not validRotValue:
        rotValue = input()
        try:
            rotValue = int(rotValue)
            validRotValue = True
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
    rotdLst = rotateList(lstToRotate, rotValue)
    print(rotdLst)
        
    

def rotateList(lst: list, rot: int) -> list:
    """Outputs a list that has been shifted over the the value 'rot'"""
    outLst = []
    for i in range(len(lst)):
        outLst.append("")
    for i in range(len(lst)):
        outLst[(i + rot) % len(lst)] = lst[i]
    return outLst


if __name__ == "__main__":
    main()
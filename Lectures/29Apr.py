# Joshua Hamaker        04/29/2025
# Lecture notes - 04/29

## Binary Search
# Searches sorted list by dividing pool in half


def main() -> None:
    arr = [1, 2, 3, 43, 55, 765, 908, 8990, 9999]
    target = 908
    ans = binarySearchSimple(arr, target)
    print(f"The location of {target} in {arr} is: {ans}")


def binarySearchSimple(A: list[int], T: int):
    retVal = None
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] < T:
            left = mid + 1
        else:
            right = mid
    if A[left] == T:
        retVal = left
    return retVal


if __name__ == '__main__':
    main()
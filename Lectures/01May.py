# Joshua Hamaker        05/01/2025
# Lecture Notes - May 01

## Soritng Algorithms
import random
import time


def main() -> None:
    array = list(range(1, 10000))
    random.shuffle(array)

    print("Bubble Sort:")
    startTime = time.time()
    arr1 = bubbleSort(array)
    endTime = time.time()
    print(f"{endTime-startTime} seconds")
    print()

    print("Selection Sort:")
    startTime = time.time()
    arr2 = selectionSort(array)
    endTime = time.time()
    print(f"{endTime-startTime} seconds")
    print()

    print("Insertion Sort:")
    startTime = time.time()
    arr3 = insertionSort(array)
    endTime = time.time()
    print(f"{endTime-startTime} seconds")
    print()
    
    print("Built-in sort")
    startTime = time.time()
    arr4 = builtinSort(array)
    endTime = time.time()
    print(f"{endTime-startTime} seconds")
    print()

    # print("Bogo Sort:")
    # startTime = time.time()
    # arr5 = bogoSort(array)
    # endTime = time.time()
    # print(f"{endTime-startTime} seconds")
    # print()


# Bubble Sort
def bubbleSort(A: list[int]) -> list[int]:
    done = False
    while not done:
        done = True
        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
                done = False
    return A


# Selection Sort
def selectionSort(A: list[int]) -> list[int]:
    for i in range(len(A) - 1):
        jMin = i
        for j in range(i+1, len(A)):
            if A[j] < A[jMin]:
                jMin = j
            if jMin != j:
                A[i], A[jMin] = A[jMin], A[i]
    return A


# Insertion Sort
def insertionSort(A: list[int]) -> list[int]:
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1
    return A


def builtinSort(A: list[int]) -> list[int]:
    A.sort()
    return A


# Bogo Sort
def bogoSort(A: list[int]) -> list[int]:
    ans = A.sort()
    while A != ans:
        random.shuffle(A)
    return A


if __name__ == '__main__':
    main()
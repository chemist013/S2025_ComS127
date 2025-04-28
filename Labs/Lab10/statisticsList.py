# Joshua Hamaker        03/28/2025
# Lab 10 - Statistics List

from os import name
import random

def main() -> None:
    statsList = generateInput()
    mean = findMean(statsList)
    median = findMedian(statsList)
    print(f"Mean: {mean:.2f}, Median: {median:.2f}")


def generateInput() -> list:
    """Generates a list of 200 - 500 ints, each between 1 - 2000"""
    outLst = []
    lstLen = random.randint(200, 500)
    for i in range(lstLen):
        outLst.append(random.randint(1, 2000))
    return outLst


def findMean(lst: list) -> float:
    """Finds the mean (average) of a given list"""
    cumSum = 0
    for i in range(len(lst)):
        cumSum += lst[i]
    mean = cumSum / len(lst)
    return mean


def findMedian(lst: list) -> float:
    """Finds the median of a given list"""
    lst.sort()
    if len(lst) % 2 == 1: # odd
        median = lst[len(lst) // 2]
    else: # even
        median = (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    return median


if __name__ == "__main__":
    main()
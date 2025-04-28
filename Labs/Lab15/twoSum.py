# Joshua Hamaker        04/27/2025
# Lab 15 - Two Sum


def main() -> None:
    lstInts, target = [7, 4, 5, 6], 11 # expected output is [0, 1] or [2, 3]
    acceptedValues = [[0, 1], [1, 0], [2, 3], [3, 2]]
    assert twoSumLoops(lstInts, target) in acceptedValues
    assert twoSumDict(lstInts, target) in acceptedValues
    assert twoSumLoopsAll(lstInts, target) == [2, 3] or [3, 2]
    assert twoSumDictAll(lstInts, target) == [2, 3] or [3, 2]


def twoSumLoops(nums: list[int], sum: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == sum:
                return [i, j]
    return []


def twoSumDict(nums: list[int], sum: int) -> list[int]:
    hash = {}
    for i in range(len(nums)):
        diff = sum - nums[i]
        if diff in hash.keys():
            return [i, hash[diff]]
        hash[nums[i]] = i
    return []


def twoSumLoopsAll(nums: list[int], sum: int) -> list[list[int]]:
    outLst = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == sum:
                outLst.append([i, j])
    return outLst


def twoSumDictAll(nums: list[int], sum: int) -> list[list[int]]:
    outLst = []
    hash = {}
    for i in range(len(nums)):
        diff = sum - nums[i]
        if diff in hash.keys():
            outLst.append([i, hash[diff]])
        hash[nums[i]] = i
    return outLst


if __name__ == '__main__':
    main()
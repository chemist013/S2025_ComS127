# Joshua Hamaker        03/04/2025
# Lecture Notes

from types import MethodDescriptorType


emptyList = []
# print(emptyList)
# print(len(emptyList))

mathOperations = ["Addition", "Integration", "Modulus", "Exponentiation", "Ceiling"]
# print(mathOperations)
# print(len(mathOperations))
# print(mathOperations[2])

differentTypes = [3, 3.14, "PI"]
# print(differentTypes)
# print(len(differentTypes))

listOfLists = [emptyList, mathOperations, differentTypes]
# print(listOfLists)
# print(len(listOfLists))

petNames = ["Fido", "Spot", "Snakey"]
# print(petNames[5]) -> ERROR

# print(listOfLists[1])
# print(listOfLists[1][2])
# print(listOfLists[1][2][4])

consoles = ["Switch", "Xbox", "Wii", "Game Boy", "PlayStation"]
games = ["Mario Kart", "Mario Baseball", "Mario"]
consolesWithGames = consoles + games
# print(consolesWithGames)

colors = ["Blue", "Yellow", "Red"] *3
# print(colors)

letters = ["J", "R", "S", "M", "T", "G", "A"]
# rsmtSlice = letters[1:5]
# print(rsmtSlice)
# tsmrSlice = letters[4:0:-1]
# print(tsmrSlice)
# print(letters)
# letters[3] = "X"
# print(letters)
# del letters[3]
# print(letters)

# List methods
    # Append
    # Pop
    # 

numbers = []
for i in range(5):
    numbers.append(i)
# print(numbers)
# numbers.append("Back of list")
# print(numbers)

def listNums(num) -> list:
    lst = []
    for i in range(num):
        lst.append(i)
    return lst
numberList = listNums(7)
# print(numberList)

str1 = "APPLE CAT!"
lst1 = []
for i in range(len(str1)-1, -1, -1):
    lst1.append(str1[i])
print(lst1)
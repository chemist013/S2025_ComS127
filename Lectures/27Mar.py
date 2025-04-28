# Joshua Hamaker        03/27/2025
# Lecture Notes 03/27

## Dictonaries

pets = {"Horsey": "Horse", "Scratchy": "Cat"} # Key: Value
pets["Rover"] = "Dog"
# Keys must be unique & immutable
# Values need not be unique or immutable

print(pets)
print(pets["Horsey"])
print()


testDict = {}
testDict["Orange"] = "Fruit"
testDict[7] = "Seven"
testDict[7] = "Six"
testDict[1.2] = "One Point Two"

print(testDict)
print(testDict[7])
print()

listDict = {}
listDict["Movies"] = []
listDict["Movies"].append("Pulp Fiction")
listDict["Movies"].append("101 Dalmatians")
listDict["Movies"].append("2001: A Space Odyssey")

listDict[17] = "Seventeen"
listDict[17] += " Hello!"

print(listDict)
print()

d1 = {1: "One", 2: "Two"}
d2 = {2: "Two", 1: "One"}

print(d1 == d2)
print()

countries = {}
countries["Australia"] = "Red Center"
countries["Russia"] = "Vodka"
countries["France"] = "Champagne"
print(countries)

del countries["France"]
print(countries)
print()

# Methods
    # keys() -> key
    # values() -> value
    # items() -> tuple w/ key & value
    # get(key) -> value of key
programingLangs = {}
programingLangs["C"] = "old"
programingLangs["JavaScript"] = "quirky"
programingLangs["Java"] = "boring"
programingLangs["Assembly"] = "low level"

for k in programingLangs.keys(): # in applies to keys only
    print(k)

print("C" in programingLangs)
print("old" in programingLangs)
print()

for v in programingLangs.values():
    print(v)

print("old" in programingLangs)
print("old" in programingLangs.values())
print()

for k, v in programingLangs.items():
    print(k, "->", v)

print("C" in programingLangs.items())
print("old" in programingLangs.items())
print(("C", "old") in programingLangs.items())
# print(programingLangs.items())
print()

print(programingLangs.get("Pyhton", "Awesome")) # defaults to 2nd arg/`None` if not found
# Joshua Hamaker        03/05/2025
# Lecture notes 03/06

## Tuples

furnitrue = "chair", "table", "chest", "wardrobe"
# can be delclared w/ & w/o parentheses; commas make the tuple
# print(furnitrue)
# print(type(furnitrue))

# print("chair", "table", "chest", "wardrobe")
# print(("chair", "table", "chest", "wardrobe"))

sciences = ("physics", "chemsitry", "biology", "psychology", "archaeology")
# print(sciences[4])
# print(sciences[len(sciences) - 1])
# print(sciences[-1]) # python thing

# print(sciences[3:0:-1])
# print(sciences[3::-1])

# for i in sciences:
#     print(i)
# print()
# for i in range(len(sciences)):
#     print(sciences[i])

colors = ("red", "green", "blue", "yellow", "purple")
# colors[2] = "chartreuse"

newColors = colors[0:2] + ("chartreuse",) + colors[3:]
# print(newColors)

pets = ("cat", "dog", "bird", "giraffe")
(pet1, pet1, pet1, pet1) = pets # assigns item by item
# print(pet1)

# REMEMBER THIS
def swap(a: any, b: any) -> tuple:
    t = a
    a = b
    b = t
    return a, b

val1 = "pen"
val2 = "pencil"
# print(val1, val2)

(val1, val2) = swap(val1, val2)
# print(val1, val2)

# OR do it the python way w/ tuples

a = "pen"
b = "pencil"
# print(a, b)

(a,b) = (b,a)
# print(a, b)
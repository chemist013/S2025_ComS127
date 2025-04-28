# Joshua Hamaker        04/24/2025
# Lecture Notes for 04/24

## Object references


cat1, y = "bonkers", "bonkers"
cat2 = y

print(cat1 is cat2) # both cat1 & cat2 (& y) refer to the same str; same obj, different references
print(hex(id(cat1)))
print(hex(id(cat2)))
print(hex(id(y)))

print()

# Seperate lists, seperate mem values
a, b = [1,2,3], [1,2,3]
print(a == b)
print(a is b)

print()

# b references a, same mem values
a = [1,2,3]
b = a
print(a is b)
print(a == b)

c = b
c.append(5) # Changing alias changes original
print(b)

print()

# Cloning lists
a = [1, 2, 3]
b = a[:]
print(a == b)
print(a is b)

b.append(4) # Changing clone doesn't change original
print(a)
print(b)

print()

a: list = [1, 2, 3]
print(a)
b = [a]*2
print(b)
a[0] = "X"
print(b)

print()

def listRef(lst: list) -> None:
    for i in range(len(lst)):
        lst[i] *= 2

a = [1, 2, 3]
print(a)
listRef(a)
print(a)

def listRefPure(lst: list) -> list:
    outLst = []
    for i in lst:
        outLst.append(i*2)
    return outLst

a = [1, 2, 3]
print(a)
listRef(a)
print(a)
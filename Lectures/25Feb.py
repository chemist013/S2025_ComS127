# Joshua Hamaker    02/25/2025
# Lecture Notes 02/25

## STRINGS
str1 = "sex" + "drugs" + "rock + roll"
print(str1)
str2 = "ithinkyouthinktoomuchofme" * 5
print(str2)

# Cannot do math w/ strs that contain numbers

# For strs: __1st index != index 1__
# str1[x] is the x-1th char of the str
# Access methods w/ dot notation
    # uc = str1.upper()
# **Notable Methods**
    # upper: str -> uppercase
    # lower: str -> lowercase
    # strip: removes white space chars @ beginning/end of str
    # count: returns number of instances of a certain char in a str
    # replace: 
    # find/index
# len: returns the cardinality of the string

strA = "Hello, world!"
for i in range(len(strA)):
    print(strA[i])
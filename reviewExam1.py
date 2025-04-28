# Joshua Hamaker        03/11/2025
# Practice/samdbox to review rof Exam 1

import random

str = "Hello, world!"


for i in range(len(str)):
    print(ord(str[i]), end=" ")


print(str.upper())
print(str.lower())
print(str.replace("l", "CAT!"))

print("l" in str)
print("0" in str)

print(str.split("l"))


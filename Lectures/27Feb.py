# Joshua Hamaker        02/27/25
# Lecture 12

#       0123456789
str1 = "APPLE CAT!"
str2 = str1[:]
print(str1)
print("-----------------")
str3 = str1[6:9]
print(str3)
print("-----------------")
str4 = str1[:5]
print(str4)
print("-----------------")
str5 = str1[6:]
print(str5)
print("-----------------")
str6 = str1[::-1]
print(str6)
print("-----------------")
str7 = ""
for i in range(len(str1)):
    str7 = (str7 + str1[len(str1)-i-1])
print(str7)
print("-----------------")
length = len(str1)
str8 = ""
for i in range(length):
    val = -(length) + i
    tempStr = str1[val]
    str8 = tempStr + str8
print(str8)
print("-----------------")
str9 = ""
for i in range(len(str1)-1, -1, -1):
    str9 = str9 + str1[i]
print(str9)
print("-----------------")
str10 = ""
lst1 = []
for i in range(len(str1)):
    lst1.append(str1[i])
tmpStr = ""
for i in range(len(str1)//2):
    tmpStr = lst1[i]
    lst1[i] = lst1[len(lst1)-i-1]
    lst1[len(lst1)-i-1] = tmpStr
for i in range(len(lst1)):
    str10 += lst1[i]
print(str10)
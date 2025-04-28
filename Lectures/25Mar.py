# Joshua Hamaker        03/25/25
# Lecture Notes 03/25

## Open/close files with open()/close()

fileRef = open("ccdata.txt", "r")

# print(fileRef)
# for line in fileRef:
#     # print(line.strip()) # can also add end="" to remove duplicate \n
#     print(line.split())

fileRef.close()

fileRef2 = open("example.txt", "w")

for i in range(10):
    fileRef2.write(str(i) + "\n")

fileRef2.close()

## Open/close files w/ with statement
# Use this instead of open()/close()

with open("ccdata.txt", "r") as f:
    print(f.read())
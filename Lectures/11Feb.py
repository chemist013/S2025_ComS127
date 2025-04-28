# Joshua Hamaker		02/11/2025
# Lecture code for Feb 11

## 'IF' statements

args = ['', 0, None, [], (), {}, False, 'Hello!', 1, [0], (0,0), {"z": 0}, True, not None]

# True = 1, False = 0

for value in args:
    if value:
        print(f"{value} resolves to True")
    else:
        print(f"{value} resolves to False")
print("")
print("")

## Switch/case w/ default in python 😭
if 5 > 7:
    print(f"5 > 7")
elif 12 == 12:
    print(f"12 = 12")
elif 3 < 5:
    print(f"3 < 5")
else:
    print("Uh-oh...")

## Boolean logic
# and
for i in [True, False]:
    for j in [True, False]:
        ans = i and j
        print(f"{i} and {j} implies {ans}")
# equivalent to:
# if a:
#     if b:
#         result = True
print("")
print("")

# or
for i in [True, False]:
    for j in [True, False]:
        ans = i or j
        print(f"{i} or {j} implies {ans}")
# equivalent to
# if a:
#     result = True
# if b:
#     result = True
print("")
print("")

# Joshua Hamaker        01/30/25
# Modules & built in functions

# void setup() {
import turtle
import math
import random
# }

## MIN() & MAX()

# smallestNum = min(3, 44, 29, 13, 1, 7);\
# print(f"The smallest number is: {smallestNum}")
# largestNum = max(3, 44, 29, 13, 1, 7)
# print(f"The largest number is: {largestNum}")

## MODULES
# turtle
# screen = turtle.Screen()
# flash = turtle.Turtle()

# flash.forward(80)
# flash.right(77)
# flash.forward(30)
# flash.pensize(5)
# flash.left(25)
# flash.forward(50)

# turtle.done()

## MATH
# print(f"The value of pi is: {math.pi}")
# print(f"The value of e is: {math.e}")
# print(f"The value of tau is: {math.tau}")

# x = float(input("Please enter a float: "))
# answer = math.acos(x)
# print(f"The arc cosine of {x} is: {answer}")

# ceilRaw = float(input("Please enter another float: "))
# ceilAns = math.ceil(ceilRaw)
# print(f"The ceiling of {ceilRaw} is: {ceilAns}")

# floorRaw = float(input("Please enter a third float: "))
# floorAns = math.floor(floorRaw)
# print(f"The ceiling of {floorRaw} is: {floorAns}")

## RANDOM
prob = random.random()
print(f"The random number is: {prob}")

rangeVal = random.randrange(1, 101)
print(f"The random number from 1 to 100 is: {rangeVal}")
# Joshua Hamaker        03/07/2025
# Lab07 - Tridecagon Turtle with L-System

# This programs iterates on the L-System privided in ThinkCSPy by adding teleportation and tridecagons

import turtle
import tridecagonTurtle
import random


def createLSystem(numIters: int, axiom: str) -> str:
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString


def processString(oldStr: str) -> str:
    """ Iterates over the input string and applies the rules of the L-system """
    newStr = ""
    for ch in oldStr:
        newStr = newStr + applyRules(ch)

    return newStr


def applyRules(ch: str) -> str:
    """ Apply the rules of the L-system to the character of the input string"""
    newStr = ""
    match ch:
        case 'F':
            newStr = 'F+H-FP'
        case 'H':
            newStr = "P+H-FF+"
        case 'P':
            newStr = "H-FP+H"
        case _:
            newStr = ch

    return newStr


def drawLsystem(aTurtle: turtle, instructions: str, angle: int, distance: int) -> None:
    """ Draws to the screen using the 'instruction' string """
    for cmd in instructions:
        match cmd:
            case 'F':
                aTurtle.forward(distance)
            case 'B':
                aTurtle.backward(distance)
            case '+':
                aTurtle.right(angle)
            case '-':
                aTurtle.left(angle)
            case 'H':
                tridecagonTurtle.tridecagonTurtle(distance, aTurtle.xcor(), aTurtle.ycor(), aTurtle)
            case 'P':
                aTurtle.teleport(random.randint(-200, 200), random.randint(-200, 200))


def main() -> None:
    inst = createLSystem(4, "F")
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.speed(10)

    drawLsystem(t, inst, 60, 10) 
    wn.exitonclick()

if __name__ == "__main__":
    main()

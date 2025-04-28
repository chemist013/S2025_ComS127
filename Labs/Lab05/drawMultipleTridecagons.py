# Joshua Hamaker        02/21/2024
# Lab05 - Draw Multiple Tridecagons

# This program iterates on tridecagonTurtle.py from Lab04
# to draw user specified number of tridecagons on the screen

import turtle

def main():
    turtleName = input(f"What should the name of this turtle be? ")
    xCord = float(input(f"What x coordinate should {turtleName} start at? "))
    yCord = float(input(f"What y coordinate should {turtleName} start at? "))
    numReps = int(input(f"How many tridecagons should {turtleName} draw? "))
    sideLength = float(input(f"How long should each side of the tridecagon be? "))
    distBetween = float(input(f"How far apart should each tridecagon be? "))

    wn = turtle.Screen()
    wn.bgcolor("#FFFFFF")
    turtleName = turtle.Turtle()

    drawMultipleTridecagons(sideLength, xCord, yCord, numReps, distBetween, turtleName)

    wn.exitonclick()

def drawMultipleTridecagons(s: float, x: float, y: float, nr: int, sr: float, t: turtle.Turtle) -> None:
    for i in range(nr):
        tridecagonTurtle(s, x, y, t)
        x = x + sr

def tridecagonTurtle(s: float, x: float, y: float, t: turtle.Turtle) -> None:
    t.ht()
    t.teleport(x,y)
    for i in range(13):
        t.fd(s)
        t.seth((i+1)*360/13)

if __name__ == "__main__":
    main()
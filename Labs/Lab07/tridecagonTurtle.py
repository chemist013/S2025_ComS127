# Joshua Hamaker        02/14/2025 # edited 03/07/2025 to fix hardcoded nonsense
# Lab 04 - Tridecagon Turtle
# This program draws a 13-sided polygon with a
# user specified start position and side length 

import turtle

def main():
    turtleName = input(f"What should the name of this turtle be? ")
    xCord = float(input(f"What x coordinate should {turtleName} start at? "))
    yCord = float(input(f"What y coordinate should {turtleName} start at? "))
    sideLength = float(input(f"How long should each side of the tridecagon be? "))

    wn = turtle.Screen()
    wn.bgcolor("#FFFFFF")
    turtleName = turtle.Turtle()

    tridecagonTurtle(sideLength, xCord, yCord, turtleName)

    wn.exitonclick()

def tridecagonTurtle(s, x, y, t):
    t.teleport(x,y)
    for i in range(13):
        t.fd(s)
        t.left(360/13)

if __name__ == "__main__":
    main()
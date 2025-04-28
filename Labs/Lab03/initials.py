# Joshua Hamaker      02/07/2025
# Lab 03 - initials

# NOTE: The documentation for the turtle module was heavily utilized in the making of this project
# It can be found here: https://docs.python.org/3/library/turtle.html

import turtle

screen = turtle.Screen()
screen.bgcolor("white")
jay = turtle.Turtle()
jay.ht()
hach = turtle.Turtle()
hach.ht()

# J
for i in range(2):
    if i == 0:
        jay.color("blue")
    else:
        jay.color("yellow")
    jay.pensize(10-5*i)
    jay.teleport(-200, 200)
    jay.seth(0)
    jay.fd(150)
    jay.teleport(-125,200)
    jay.seth(270)
    jay.fd(150)
    jay.seth(180)
    jay.fd(75)

# H
for i in range(2):
    if i==0:
        hach.color("#CCB7FF")
    else:
        hach.color("palegreen")
    hach.pensize(10-5*i)
    hach.teleport(50,-50)
    hach.seth(270)
    hach.fd(150)
    hach.teleport(200,-50)
    hach.seth(270)
    hach.fd(150)
    hach.teleport(50,-125)
    hach.seth(0)
    hach.fd(150)

turtle.exitonclick()
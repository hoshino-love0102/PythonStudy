from turtle import *
speed(3)
penup()
goto(100, 100)
pendown()

for _ in range(3):
    forward(100)
    right(120)

penup()
goto(-200, 200)
pendown()

for _ in range(4):
    forward(100)
    right(90)

exitonclick()

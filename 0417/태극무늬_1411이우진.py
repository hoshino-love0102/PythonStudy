from turtle import *
import colorsys

bgcolor("black")
speed(0)
pensize(2)

a = 0
di = 1

for i in range(200):
    r, g, b = colorsys.hsv_to_rgb(a, 1, 1)
    pencolor(r, g, b)
    
    forward(di)
    right(119)
    di += 2
    a += 0.005 

exitonclick()
from turtle import *

n=int(input())
length = 100

angle = 360 / n
speed(9)
for i in range(n):
    forward(length)
    right(angle)

exitonclick()
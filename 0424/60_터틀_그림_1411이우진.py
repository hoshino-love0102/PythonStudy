from turtle import *

d = 10

def turn_right():
    fd(d)

def turn_up():
    left(90)
    fd(d)

def turn_left():
    left(180)
    fd(d)

def turn_down():
    right(90)
    fd(d)

def blank():
    clear()

def keyboard():
    shape("turtle")
    speed(0)
    onkeypress(turn_right, "Right")
    onkeypress(turn_up, "Up")
    onkeypress(turn_left, "Left")
    onkeypress(turn_down, "Down")
    onkeypress(blank, "Escape")
    listen()

def mouse():
    speed(0)
    pensize(2)
    onscreenclick(goto)
    onkeypress(blank, "Escape")
    listen()

select = input("키보드(1) 마우스(2): ")

if select == "1":
    keyboard()
elif select == "2":
    mouse()

mainloop()

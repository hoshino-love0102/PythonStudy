import turtle

def a(x, a=0.005, b=0, c=0):
    return a * x ** 2 + b * x + c

def draw_axes():
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.color("gray")
    
    # x축
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.goto(300, 0)

    # y축
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.goto(0, 200)

def draw_graph():
    graph = turtle.Turtle()
    graph.speed(0)
    graph.color("blue")
    graph.penup()

    x = -300
    y = a(x)
    graph.goto(x, y)
    graph.pendown()

    while x <= 300:
        y = a(x)
        graph.goto(x, y)
        x += 1

turtle.setup(width=800, height=600)
draw_axes()
draw_graph()
turtle.done()

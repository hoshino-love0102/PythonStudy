def get():
    a1, b1 = map(float, input("(x1, y1): ").split(','))
    a2, b2 = map(float, input("(x2, y2): ").split(','))
    return a1, b1, a2, b2

def get_line(a1, b1, a2, b2):
    if a1 == a2:
        x0 = int(a1) if a1.is_integer() else a1
        return f"x = {x0}"
    else:
        s = (b2 - b1) / (a2 - a1)
        y = b1 - s * a1
        return f"y = {s}x + ({y})"

x1, y1, x2, y2 = get()
line = get_line(x1, y1, x2, y2)
print(line)
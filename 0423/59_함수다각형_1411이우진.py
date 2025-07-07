from turtle import *

def input_data():
    x = int(input("이동할 x좌표 입력: "))
    y = int(input("이동할 y좌표 입력: "))
    a = int(input("한 변의 길이 입력: "))
    n = int(input("변의 개수(n ≥ 3) 입력: "))
    
    if n < 3:
        print("도형은 최소 3변 이상이어야 합니다.")
        return input_data()
    return x, y, a, n

def moving(x, y):
    up()
    goto(x, y)
    down()

def polygon(a, n):
    angle = 360 / n
    for _ in range(n):
        forward(a)
        left(angle)

while True:
    print("===== 도형 그리기 =====")
    x, y, a, n = input_data()
    moving(x, y)
    polygon(a, n)
    
    con = int(input("계속하시겠습니까? (1: 예, 그 외: 종료): "))
    if con != 1:
        break

exitonclick()

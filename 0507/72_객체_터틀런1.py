from turtle import Screen, Turtle
import random
import time

# 기본 화면 세팅
screen = Screen()
screen.setup(width=600, height=600)
screen.title("거북이 생존 게임")
screen.bgcolor("orange")
screen.tracer(0)

# 플레이어 생성
player = Turtle("turtle")
player.color("green")
player.penup()

# 빌런 생성
chaser = Turtle("turtle")
chaser.color("red")
chaser.penup()
chaser.goto(200, 200)

# 먹이 생성
food = Turtle("circle")
food.color("blue")
food.penup()

def relocate_food():
    food.goto(random.randint(-250, 250), random.randint(-250, 250))

relocate_food()

# 점수
score = 0
score_writer = Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-270, 260)
score_writer.write(f"Score: {score}", font=("Arial", 16, "bold"))

def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=("Arial", 16, "bold"))

# 키 상태 관리
key_state = {"Up": False, "Down": False, "Left": False, "Right": False}

# 키 누름 처리
def key_press(event):
    if event.keysym in key_state:
        key_state[event.keysym] = True

# 키 뗌 처리
def key_release(event):
    if event.keysym in key_state:
        key_state[event.keysym] = False

# tkinter 이벤트 바인딩
canvas = screen.getcanvas()
canvas.bind("<KeyPress>", key_press)
canvas.bind("<KeyRelease>", key_release)
canvas.focus_set()

# 상수
PLAYER_SPEED = 5
CHASER_SPEED = 1.5
BOUND = 280
game_over = False

# 게임 루프
while not game_over:
    # 플레이어 이동
    x, y = player.xcor(), player.ycor()
    if key_state["Up"]:
        y = min(y + PLAYER_SPEED, BOUND)
    if key_state["Down"]:
        y = max(y - PLAYER_SPEED, -BOUND)
    if key_state["Left"]:
        x = max(x - PLAYER_SPEED, -BOUND)
    if key_state["Right"]:
        x = min(x + PLAYER_SPEED, BOUND)
    player.goto(x, y)

    # 빌런 추적
    chaser.setheading(chaser.towards(player))
    chaser.forward(CHASER_SPEED)

    # 충돌 체크
    if chaser.distance(player) < 15:
        print("게임 오버! 잡혔습니다.")
        break

    # 먹이 획득
    if player.distance(food) < 20:
        score += 1
        update_score()
        relocate_food()

    screen.update()
    time.sleep(0.01)

screen.mainloop()


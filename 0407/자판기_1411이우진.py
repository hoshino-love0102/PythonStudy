a = 0

while a <= 5:
    b = int(input("돈 입력: "))
    if b == 800:
        print("맛있는 음료 드세요")
    elif b > 800:
        print(f"맛있는 음료 드시고 잔돈:{b - 800}")
    else:
        print(f"가격을 확인해주세요.\n{a}")
    if b >= 800:
        a += 1

print("매진")

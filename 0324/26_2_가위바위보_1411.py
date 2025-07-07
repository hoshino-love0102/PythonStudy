import random
user = int(input("1: 가위, 2: 바위, 3: 보: "))

if user == 1:
    user_str = "가위"
elif user == 2:
    user_str = "바위"
else:
    user_str = "보"
com_choice = random.randint(1, 3)
if com_choice == 1:
    com_str = "가위"
elif com_choice == 2:
    com_str = "바위"
else:
    com_str = "보"
if user == com_choice:
    print("비김")
elif (user == 1 and com_choice == 3) or (user == 2 and com_choice == 1) or (user == 3 and com_choice == 2):
    print(f"이겼음 {user_str} {com_str}")
else:
    print(f"졌음 {user_str} {com_str}")

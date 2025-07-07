import random
def roll():
    return random.randint(1, 6)
user = input("두 개의 숫자를 공백으로 구분하여 입력하세요: ")
userl = list(map(int, user.split()))
dice = [roll(), roll()]
if sorted(userl) == sorted(dice):
    print("1등!")
elif len(set(userl).intersection(set(dice))) == 1:
    print("2등!")
else:
    print("3등!")
print(f"주사위 결과: {dice}")
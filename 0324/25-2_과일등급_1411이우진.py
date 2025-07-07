f=int(input("과일 무게(g): "))
if 375<=f or 210>f:
    print("\"판정 불가\"")
elif 300<=f and 370>f:
    print("\"특\"")
elif 250<=f and 300>f:
    print("\"상\"")
elif 210<=f and 250>f:
    print("\"보통\"")
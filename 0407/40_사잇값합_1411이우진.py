import random

while True:
    t=0
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if a > b:
        a, b = b, a
    for i in range(a,b+1):
        t=t+i
    print(f"{a}부터 {b}까지의 자연수 합: {t}")
    if a == b:
        break
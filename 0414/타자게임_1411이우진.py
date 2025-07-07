import random
import time

words = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
correct = 0

print("[타자게임]준비되면 엔터")
input()

start = time.time()
s=0

while correct < 5:
    q = random.choice(words)
    print(f"\n문제 {s + 1}: {q}")
    ans = input("입력: ")

    if ans == q:
        print("pass")
        correct += 1
    else:
        print("fail")
    s+=1
end = time.time()
re = end - start

print(f"걸린 시간: {re:.2f}초")

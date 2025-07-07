import random
import time

words = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
correct = 0

print("[타자게임] 준비되면 엔터")
input()

start = time.time()

random.shuffle(words) #리스트 섞기
s = 0

while correct < 5 and s < len(words): #맞춘게 5개보다 적고 리스트안에보다 번호가 적을때까지 반복 
    q = words[s]
    print(f"\n문제 {s + 1}: {q}")
    ans = input("입력: ")

    if ans == q:
        print("pass")
        correct += 1
    else:
        print("fail")
    s += 1

end = time.time()
re = end - start
print(f"\n걸린 시간: {re:.2f}초")
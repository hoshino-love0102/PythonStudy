num = int(input("어떤 수의 배수? "))
print(f"{num}의 배수:")
for i in range(50, 101):
    if i % num == 0:
        print(i)
n = int(input("자연수: "))

for i in range(n, 0, -1):
    if n % i == 0:
        print(i)

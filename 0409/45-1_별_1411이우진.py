n = int(input("행 수: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

height=int(input("행 수: "))

for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
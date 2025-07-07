for i in range(1, 7):
    for j in range(1, 7):
        print(f"({i},{j})", end=" ")
    print()

for i in range(1, 7):
    for j in range(1, 7):
        print(f"({j},{i})",end="")
    print()

for i in range(1, 7):
    for j in range(1, 7):
        if i == j:
            print("     ", end=" ")
        else:
            print(f"({i},{j})", end=" ")
    print()

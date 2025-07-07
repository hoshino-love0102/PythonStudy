rows=int(input("행 수: "))
col=int(input("열 수: "))

num = 1
for i in range(rows):
    for j in range(col):
        print(f"{num:2}", end=' ')
        num += 1
    print()

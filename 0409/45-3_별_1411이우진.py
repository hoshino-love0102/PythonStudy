n = int(input("행 수: "))
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,a-i+1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
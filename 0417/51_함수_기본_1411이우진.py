def a123(n):
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = a[i - 1] + i
    return a[n]

a = int(input())
print(a123(a))
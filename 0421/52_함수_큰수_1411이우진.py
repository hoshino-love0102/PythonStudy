def maxp(a, b):
    if a > b:
        return a
    else:
        return b
print(f'큰 수: {maxp(10, 20)}')
a, b = map(int, input().split())
print(f'큰 수: {maxp(a, b)}')

def sub1(x):
    a = x * 100
    return a

def sub2(x):
    global a
    a = x * 100
    return a
a = 10
print(sub1(a))
print(a)
print(sub2(a))
print(a)

# def sub1(lst):
#     mylst = list(range(7, 11))
#     print(f'sub1 함수 리스트: {mylst}')

# def sub2(lst):
#     global mylst
#     mylst = list(range(1, 5))
#     print(f'sub2 함수 리스트: {mylst}')

#
# mylst = list(range(10, 50, 10))
# sub1(mylst)
# sub2(mylst)
# print(f'메인함수 리스트: {mylst}')

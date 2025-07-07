#51-1 함수기본
def fun_s(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return fun_s
print(fun_s(10))
print(fun_s(100))
print(fun_s(1000))

#51-2 함수기본
def fun_fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(fun_fact(5))
print(fun_fact(10))

def f_avg(lst):
    return sum(lst) / len(lst)

def f_var(lst):
    avg = f_avg(lst)
    s = 0
    for i in lst:
        s += (i - avg) ** 2
    return s / len(lst)

def f_std(lst):
    return f_var(lst) ** 0.5

def f_comm(lst):
    mi = lst[0]
    mx = lst[0]
    for i in lst:
        if i < mi:
            mi = i
        if i > mx:
            mx = i
    return mi, mx

nums = list(map(int, input("숫자 입력").split()))
    
print("리스트:", nums)
print("평균:", f_avg(nums))
print("분산:", f_var(nums))
print("표준편차:", f_std(nums))
min1, max1 = f_comm(nums)
print("최소값:", min1)
print("최대값:", max1)
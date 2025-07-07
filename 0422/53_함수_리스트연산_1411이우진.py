def lst_create():
    data = input("숫자(공백으로 분리): ").split()
    lst = []
    for x in data:
        try:
            lst.append(float(x))
        except ValueError:
            pass
    return lst

def lst_append(lst):
    while True:
        s = input("추가 숫자: ")
        try:
            num = float(s)
            lst.append(num)
        except ValueError:
            break
    return lst

def lst_cal(lst):
    total = sum(lst)
    avg = total / len(lst) if lst else 0
    return total, avg

def lst_print(lst, result):
    total, avg = result
    print("*** 계산 결과")
    print("목록:", lst)
    print(f"합계: {total:.2f}  평균: {avg:.2f}")

lst_s = lst_create()
lst_f = lst_append(lst_s)
result = lst_cal(lst_f)
lst_print(lst_f, result)

import math

lst = list(range(1, 11))

mean = sum(lst) / len(lst)
print(f'평균:{mean}')

total = 0
for x in lst:
    total += (x - mean) ** 2
var = total / len(lst)
print(f"분산:{var}")

std=math.sqrt(var)
print(f'표준편차:{std}')

gcd = math.gcd(*lst)
lcm = math.lcm(*lst)
print(f'최대공배수:{gcd}, 최소공배수:{lcm}')
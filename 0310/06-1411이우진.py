m=int(input('예금 금액(원):' ))
rate=float(input('예금 이율(%): '))
d=int(input('예금 기간(년): '))
print('##############################')
result=int(m+(m*rate*0.01*d))
print(f'{m}원을 {rate}% 이율로 {d}년간 예치 후 원리합계는 {result}원') 
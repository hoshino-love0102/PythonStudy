print('#'*22)
print("{:^15}".format("BMI 계산 프로그램"))
print('#'*22)
he=float(input('키(cm):'))     #he=키
we=float(input('몸무게(kg):'))  #we=무게
BMI=we/(he/100)**2
print(f'당신의 BMI 지수는 {round(BMI,2)}입니다.')
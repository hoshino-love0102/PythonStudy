while True:
    a=int(input("5의 배수 입력: "))

    if a==0:
        break
    if a%5==0:
        print("5의 배수입니다.")
    else:
        print("5의 배수가 아닙니다")
print("프로그램 종료")
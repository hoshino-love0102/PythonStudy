print("##예외 처리1##")

while True:
    try:
        n1 = int(input("숫자 입력: "))
    except ValueError:
        print("숫자만 입력하세요.")
    else:
        print(f"입력한 숫자: {n1}")
        break

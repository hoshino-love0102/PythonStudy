print("Hello", end=' ')
print("World")
# 입력값 받기
w, h, b = map(int, input().split())

# 저장 용량 계산
bit_size = w * h * b  # 이미지 전체의 비트 크기
byte_size = bit_size / 8  # 바이트 단위로 변환
mb_size = byte_size / 1024 / 1024  # 메가바이트(MB) 단위로 변환

# 소수점 셋째 자리에서 반올림하여 둘째 자리까지 출력
print(f"{round(mb_size, 2)} MB")

print('#'*20)
text = "{:^20}".format("분초 계산 프로그램")
print(text)
print('#'*20)
s=int(input('초 입력: '))
m=s//60
print(f'{m}분 {s%60}초')
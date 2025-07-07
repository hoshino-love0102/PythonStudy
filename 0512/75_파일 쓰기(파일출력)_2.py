f = open("data_3.txt", "w")

while True:
    content = input("내용 입력: ")

    if content != "":
        f.write(content + "\n")
    else:
        break

f.close()
print("정상 종료")

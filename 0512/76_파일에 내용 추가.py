f = open("data_2.txt", "a")

for i in range(11, 20):
    content = str(i) + "번째 줄입니다.\n"
    f.write(content)

f.close()

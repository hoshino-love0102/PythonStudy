f = open("data_2.txt", "w")
for i in range(1, 11):
    line = str(i) + "\n"
    f.write(line)
f.close()
print("정상 종료")

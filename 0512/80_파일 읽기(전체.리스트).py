# 한 줄씩 읽기
# readlines()
f = open("data_2.txt", "r")
lines = f.readlines()
print(lines)

for line in lines:
    line = line.strip()
    print(line)

f.close()

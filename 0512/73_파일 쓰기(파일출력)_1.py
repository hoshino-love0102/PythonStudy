# 바로 쓰기. 표준입력받아 쓰기
f = open("data_1.txt", "w")
f.write("안녕하세요!\n")     # 바로 쓰기
content = input()            # 표준입력받아 쓰기
f.write(f"{content}\n")
f.close()

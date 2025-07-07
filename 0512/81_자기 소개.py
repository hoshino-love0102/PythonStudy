name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
school = input("학교를 입력하세요: ")

f = open("me.txt", "w")
f.write("이름: " + name + "\n")
f.write("나이: " + age + "\n")
f.write("학교: " + school + "\n")
f.close()

print("me.txt에 저장 완료!")
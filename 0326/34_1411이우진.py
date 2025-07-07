fruit = []
while len(fruit) < 5:
    fruit_input = input("과일을 입력하세요: ")
    if fruit_input in fruit:
        print("이미 리스트에 있는 과일입니다.")
    else:
        fruit.append(fruit_input)
print("최종 과일 리스트:", fruit)

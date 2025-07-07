hap = 0
count = 0

while True:
    score = float(input("점수를 입력하세요 (음수 입력 시 종료): "))
    if score < 0:
        break
    hap += score
    count += 1
if count > 0:
    avg = hap / count
    print(f"합계: {hap}, 평균: {avg}")
else:
    print("입력된 점수가 없습니다.")

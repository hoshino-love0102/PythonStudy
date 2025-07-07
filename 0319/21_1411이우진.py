h=float(input("키(cm): "))
w=float(input("체중(kg): "))
print("#"*20)
if 190>h>=130 and 100>w>=25:
    print("이용가능")
else:
    print("이용 불가능")
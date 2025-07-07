a = input("영문 문자열을 입력하세요: ")
a = a.lower()
n = 'aeiou'
vow_c = 0
con_c = 0

for char in a:
    if char.isalpha():
        if char in n:
            con_c += 1
        else:
            vow_c += 1

print("모음 개수:", vow_c)
print("자음 개수:", con_c)


# a = input("영문 문자열을 입력하세요: ")
# a = a.lower()
# n = 'aeiou'
# c = 'bcdfghjklmnpqrstuvwxwz'
# vow_c = 0
# con_c = 0

# for char in a:
#     if char in n:
#         con_c += 1
#     elif char in c:
#         vow_c += 1

# print("모음 개수:", vow_c)
# print("자음 개수:", con_c)
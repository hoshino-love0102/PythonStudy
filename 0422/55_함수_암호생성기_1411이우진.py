import random

def genPass():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    passwd = ""
    for _ in range(8):
        passwd += random.choice(chars)
    return passwd
for i in range(3):
    result = genPass()
    print(f"암호 {i+1}: \033[31m{result}\033[0m")

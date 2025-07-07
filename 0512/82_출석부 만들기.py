with open("attendance.txt", "w") as f:
    for i in range(5):
        f.write(f"{i}번 {name}")
        name=input(f"{i+1}번: ")
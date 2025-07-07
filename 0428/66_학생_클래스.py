class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def introduce(self):
        print(f"안녕 나는 {self.grade}학년 {self.name}이야")

s1=Student("지민",5)
s1.introduce()
import random as r
print(r.random())
print(r.uniform(10,11))
print(r.randint(10,100))
print(r.randrange(10,100,10))
a_list=list(range(1,10))
print(r.choice(a_list))
print(r.choice(a_list,k=3))
teacher = ['미아람','이승호','강진아','정다혜']
r.shuffle(teacher)
print(teacher)
print(r.choice(teacher))
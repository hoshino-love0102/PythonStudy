class MemberInfo:
    def __init__(self,idx,passwd,name):
        self.idx=idx
        self.passwd=passwd
        self.name=name
    
    def getMember(self):
        return f'{self.idx}, {self.passwd}, {self.name}'
    
my_member = MemberInfo('king', '123456', '홍길동')
print(my_member.getMember())
class BankAccount:
    def __init__(self, acnt, balance=0):
        self.acnt = acnt
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print(f"{amt}원 입금")
        print(f"현재 잔액: {self.balance}원")

    def withdraw(self, amt):
        if amt > self.balance:
            print("잔액 부족")
        else:
            self.balance -= amt
            print(f"{amt}원 출금")
            print(f"현재 잔액: {self.balance}원")

a = BankAccount('123-456')
a.deposit(10000)
a.withdraw(5000)

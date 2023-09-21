class BankAccount:
    def __init__(self):
        self.__balance = 0  # private 변수 : 숨겨짐
        self.name = "홍길동"

    def show_balance(self):
        print("현재 잔액 : ", self.__balance)

    def get_name(self):
        return self.name
    
    def deposit(self):
        deposit_money = int(input("예금액 입력 : "))
        self.__balance += deposit_money
    
    def withdraw(self):
        withdraw_money = int(input("출금액 입력 : "))
        if self.__balance >= withdraw_money:
            self.__balance -= withdraw_money
        else:
            print('잔액이 부족합니다.')
    
acc = BankAccount()
acc.show_balance()
print(acc.get_name())

# 인스턴스 변수의 값 변경
acc.__balance = 1000 # 값 변경 불가
acc.name = "이몽룡" # 변경 가능
acc.show_balance()
print(acc.get_name())

print("--------------------")
acc.show_balance()
acc.deposit()
acc.withdraw()
acc.show_balance()

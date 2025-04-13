# 属性封装
class BankAccount(object):
    __balance=0
    def __init__(self,init_amount=0):
        self.__balance=init_amount
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self,withdraw_amount):
        self.__balance-=withdraw_amount
        
    
    def get_balance(self):
        return self.__balance
        
account=BankAccount(100)
print(account.get_balance())
account.withdraw(10)
print(account.get_balance())
account.deposit(20)
print(account.get_balance())
    
    
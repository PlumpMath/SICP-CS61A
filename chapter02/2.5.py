#OOP
class Account:
    interest = 0.02 
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


zhang = Account('zhanglanqing')
print(hasattr(zhang,'deposit'))
f = getattr(zhang, 'deposit')#方法
g = getattr(Account,'deposit')#函数
print(f)
print(g)
g(zhang,20)
zhang.interest = 0.08
print(zhang.interest)
li = Account('li')
print(li.interest)



class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        #这里的self.withdraw是因为后面继承的，要将self绑定到新的而不是旧的
        return Account.withdraw(self, amount + self.withdraw_charge)


checking = CheckingAccount('Sam')
checking.deposit(1)
# deposit is called with self bound to an instance of CheckingAccount, not of Account.


#这样之后就不能使用多态了
def deposit_all(winners, amount=5):
    for account in winners:
        Account.deposit(account, amount)

#这样是能使用多态的
def deposit_all(winners, amount=5):
    for account in winners:
        account.deposit(amount)



#多重继承
class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1           # A free dollar!

#如果遇见两个继承中都出现的变量python将按照下面的顺序执行
#AsSeenOnTVAccount, CheckingAccount, SavingsAccount, Account, object


#查看继承关系
print([c.__name__ for c in AsSeenOnTVAccount.mro()])


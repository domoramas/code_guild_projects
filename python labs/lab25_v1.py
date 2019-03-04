#ATM

class ATM:
    def __init__(self, balance = 0, int_rate = .01): #initializer with balance and interest rate defaults
        self.balance = balance 
        self.int_rate = int_rate

    def check_balance(self):  
        return f'{self.balance}'
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def __check_withdrawl(self, amount): #checks to see if withdrawl will cause negative balance
        if (self.balance - amount) >= 0:
            return True  
        return False
    def withdraw(self, amount): #takes money from balance
        if self.__check_withdrawl(amount):
            self.balance -= amount
            return self.balance
        return f"insufficient funds"

    def calc_intrest(self):
        return (self.balance * self.int_rate)
    
money = ATM(100)
print(money.check_balance())
money.deposit(200)
print(money.check_balance())
print(money.withdraw(500))


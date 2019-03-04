#ATM

class ATM:
    def __init__(self, balance = 0, int_rate = .01, trans = []): #initializer with balance and interest rate defaults
        self.balance = balance 
        self.int_rate = int_rate
        self.trans = []
    def check_balance(self):  
        return f'{self.balance}'
    
    def deposit(self,amount):
        self.balance += amount
        self.trans.append(f"user deposited ${amount}")
        return self.balance

    def __check_withdrawl(self, amount): #checks to see if withdrawl will cause negative balance
        if (self.balance - amount) >= 0:
            return True  
        return False

    def withdraw(self, amount): #takes money from balance
        if self.__check_withdrawl(amount):
            self.balance -= amount
            self.trans.append(f"user withdrew ${amount}")
            return self.balance
        return (f"insufficient funds")

    def calc_intrest(self):
        return (self.balance * self.int_rate)
    
    def print_transactions(self):
        for i in range(len(self.trans)):
            print (self.trans[i])


#REPL
account = ATM()
while True:
    user_command = input("What would you like to do (deposit, withdrawl, check balance, histrory)? ")
    if user_command == "deposit":
        amount = input("How much would you like to deposit?: $")
        try:
            account.deposit(int(amount))
            print(f"Your deposit of ${amount} has been added to your account")
        except:
            print("Please enter a valid amount.")
    elif user_command == "withdrawl":
        amount = input("How much would you like to withdraw?: $")
        try:
            if account.withdraw(int(amount)) == "insufficient funds": 
                print ("insufficient funds")
            else:
                print(f"Your withdrawl of ${amount} has been deducted from your account ")
        except:
            "invalid input"   
    elif user_command == "check balance":
        print(str(account.check_balance(),end='\n'))
    elif user_command == "history":
        account.print_transactions()
    exit_string = input("Would you like to do anything else?(y or n): ")
    if exit_string == "n":
            break





#instance  method, class method and static method
#class method : method that are not bound to be an instance  of class and class method can only access and modify class variable but not instance variable
#instance variable: can access class variable as well as instance variable
#static variable : con not access class attribute or instance attribute and static method is define using @staticmethod decorator

class Account:
    Mini_bal=1000 #class variable
    
    def __init__(self, account_no, name, balance):
        self.account_no=account_no #instance variable
        self.name=name
        self.balance=balance
        
        
    def display(self):
        print('Account Number:', self.account_no)
        print('Account Holder Name:', self.name)
        print('Available Balance :', self.balance)
        
    def deposit(self, amount):
        self.balance=self.balance+amount
    @classmethod
    def displayMinBal(cls):
        print('Minimum Balance:',Account.Mini_bal)
        
        
        
    def withdraw(self, amount):
        r=Account.check_balance(amount,self.balance)
        if r==-1:
            print('Insufficient balance')
        else:
            self.balance=self.balance-amount
            
        
        
    @classmethod
    def check_balance(amount,balance):
        if amount>balance:
            return -1
        else:
            return 1
        
        
a=Account(2001, 'Raj',50000)
b=Account(2002, 'Ram',70000)
a.displayMinBal()
a.display()
a.withdraw(5000)

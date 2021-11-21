# We have provided you with a stub class called Account that represents a bank account. 
# Please fill out the stub functions, then write a program that creates 3 unique instances of the class, and store them in a data structure of your choice. 
# Explain your thought process behind choosing a data structure.
class Account:
    def __init__(self, uuid, name, balance):
        self.id = uuid
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Deposited RM{amount} to the account, balance in user {self.name} is now RM{self.balance}')

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f'Withdrawed RM{amount} from the account, balance in user {self.name} is now RM{self.balance}')
        
    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"
    
# create 3 unique instances of the class
user_account_instances = {}
user_account_instances['A1'] = Account('A1', 'Ali', 10000)
user_account_instances['A2'] = Account('A2', 'Ahmad', 1900)
user_account_instances['A3'] = Account('A3', 'Aireen', 100340)

# reason why using dictionary to store those data;
# 1) for a data with a unique value, it is easier to store data in key-values structure
# 2) Easier to keep track and manipulate compare to others like list, tuple or set
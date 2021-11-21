# We have received a request to create a new class DevAccount inheriting from the Account class for testing and development purposes. 
# This new class contains the additional functions:

# Get Balance
# Set Balance
# Transfer to other account
# Please implement the afformentioned class and their functions

from question_1  import Account

class DevAccount(Account):
    def get_balance(self):
        return self.balance
    def set_balance(self, amount):
        self.balance = amount
    def transfer_to_other_account(self, target_account, amount):
        curr_balance = self.get_balance()
        # if not enough money to transfer
        if curr_balance <= amount:
            print('Insufficient funds. Process declined.')
            return
        
        left_balance = curr_balance - amount
        self.set_balance(left_balance)     
        target_account.deposit(amount)
        print(f'Process successful. RM{amount} has been deducted from your account.')
        print(f'Your previous balance was RM{curr_balance} and your current balance is now RM{left_balance}')

# create 3 unique instances of the class
user_account_instances = {}
user_account_instances['A1'] = DevAccount('A1', 'Ali', 10000)
user_account_instances['A2'] = DevAccount('A2', 'Ahmad', 1900)
user_account_instances['A3'] = DevAccount('A3', 'Aireen', 100340)

user_account_instances['A2'].transfer_to_other_account(user_account_instances['A3'], 100)


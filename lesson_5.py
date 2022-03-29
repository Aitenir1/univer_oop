class BankAccount:
    def __init__(self, name, number, balance):
        self.account_name = name
        self.number = number
        self.balance = balance
    
    def deposit(self, ammount):
        self.balance += ammount
    
    def withdrawal(self, ammount):
        self.balance -= ammount
    
    def display(self):
        print(f'Number: {self.number} \nAccount name: {self.account_name} \nBalance: {self.balance}')
    
number, name, balance = input('Number: '), input('Account name: '), int(input('Balance: '))

b = BankAccount(name, number, balance)

b.deposit(1000)
b.withdrawal(200)
b.display()
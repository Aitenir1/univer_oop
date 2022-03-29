class Person:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def log_in(self, name, password):
        if self.name != name:
            raise Exception('Incorrect login')
        
        if self.password != password:
            raise Exception('Incorrect password')

class Manager(Person):
    def __init__(self, name, email, password, balance, goods, costs):
        super().__init__(name, email, password)
        self.balance= balance
        self.goods = {i:j for i, j in zip(goods, costs)}
    
    def buy_new(self, good, cost):
        self.goods[good] = cost

    # def __str__(self):
    #     return '\n'.join(self.goods)

class Salesman(Person):
    def __init__(self, name, email, password, boss):
        super().__init__(name, email, password)
        self.boss = boss


arafat = Person('Arafat', 'arafat2003@gmail.com', '123456789')


aitenir = Manager('Aitenir', 'aitenir_super@gmail.com', '192837456', 21431238471362481326481236,
    ['Book', 'Display', 'Soap', 'Mouse', 'Snake', 'Elephante', 'Azamat'],
    [400, 20000, 100, 500, 300000, 1000000, 50]
)
aitenir.buy_new('Klaviatura', 5000)

adil = Salesman('Adil', 'adilchik@gmail.com', 'aitenironelove', aitenir)
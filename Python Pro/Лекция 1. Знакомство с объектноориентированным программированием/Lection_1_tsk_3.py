class Order:

    def __init__(self, last_name, first_name, patronymic, bag=None):
        self.bag = bag
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.bag = []
        self.summa = 0

    def add_to_bag(self, goods, price):
        self.bag.append((goods, price))

    def to_pay(self):
        for el in self.bag:
            self.summa += el[1]
        return self.summa

    def __str__(self):
        return f'Customer: {self.last_name} {self.first_name} {self.patronymic}\nOrder: {self.bag}\nTo Pay: {self.summa} USD'


order1 = Order('Соболев', 'Гордей', 'Пётрович')
order1.add_to_bag('Car', 150)
order1.add_to_bag('Table', 300)
order1.add_to_bag('Bread', 250)
order1.to_pay()
print(order1)


order2 = Order('Рыбаков', 'Максимилиан', 'Семёнович')
order2.add_to_bag('Fish', 1000)
order2.add_to_bag('Candy', 25)
order2.add_to_bag('House', 1350)
order2.to_pay()
print(order2)


order3 = Order('Павлов', 'Оскар', 'Лаврентьевич')
order3.add_to_bag('Pizza', 190)
order3.add_to_bag('Milk', 40)
order3.add_to_bag('Cheese', 72)
order3.to_pay()
print(order3)

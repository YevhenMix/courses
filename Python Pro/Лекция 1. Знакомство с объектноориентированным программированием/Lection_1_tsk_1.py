class Goods:

    def __init__(self, price, desc, size):
        self.price = price
        self.desc = desc
        self.size = size

    def __str__(self):
        return f'Goods: {self.desc}\nSize: {self.size} mm\nPrice: {self.price} UAH'


car = Goods(1500000, 'Opel', '200x250x500')
bread = Goods(5, 'White bread', '10x20x30')
table = Goods(2500, 'Office table', '900x500x350')

print(car)
print(bread)
print(table)

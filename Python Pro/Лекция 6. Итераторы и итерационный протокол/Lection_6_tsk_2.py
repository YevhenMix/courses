"""2) Модифицируете класс Заказ (задание Лекции 1) добавив реализацию протокола последовательностей и итерационного
протокола."""


class OrderIterator:

    def __init__(self, wrap):
        self.wrap = wrap
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.wrap):
            self.index += 1
            return self.wrap[self.index - 1]
        else:
            raise StopIteration


class Order:

    def __init__(self, last_name, first_name, patronymic):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.bag = []
        self.summa = 0

    def add_to_bag(self, goods, price, quantity=1):
        self.bag.append((goods, quantity))
        self.summa += price * quantity

    def __iter__(self):
        return OrderIterator(self.bag)

    def __getitem__(self, index):
        if isinstance(index, slice):
            if (index.start and index.start < -len(self.bag)) or (index.stop and index.stop > len(self.bag)):
                raise IndexError
            else:
                result = []
                if index.step and index.step > 0 or index.step is None:
                    start = 0 if index.start is None else index.start
                    stop = len(self.bag) if index.stop is None else index.stop
                    step = 1 if index.step is None else index.step
                    for i in range(start, stop, step):
                        result.append(self.bag[i])
                elif index.step and index.step < 0:
                    start = -1 if index.start is None else index.start
                    stop = -len(self.bag)-1 if index.stop is None else index.stop
                    step = index.step
                    for i in range(start, stop, step):
                        result.append(self.bag[i])
                return result

        if isinstance(index, int):
            if index < len(self.bag):
                return self.bag[index]
            else:
                raise IndexError

        raise TypeError

    def __len__(self):
        return len(self.bag)

    def __str__(self):
        return f'Customer: {self.last_name} {self.first_name} {self.patronymic}\nOrder: {self.bag}\nTo Pay: {self.summa} UAH'


order1 = Order('Соболев', 'Гордей', 'Пётрович')
order1.add_to_bag('Car', 150)
order1.add_to_bag('Table', 300)
order1.add_to_bag('Bread', 250, 5)
order1.add_to_bag('Fish', 1000, 2)
order1.add_to_bag('Candy', 25, 2)
order1.add_to_bag('House', 1350)
print(order1)

for i in order1.__iter__():
    print(i)

print(order1.__getitem__(2))
print(len(order1))

print(order1[3:])

class Customer:

    def __init__(self, last_name, first_name, patronymic, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def __str__(self):
        return f'Yor full name: {self.last_name} {self.first_name} {self.patronymic}\nYour number: {self.phone_number}'


customer1 = Customer('Соболев', 'Гордей', 'Пётрович', '067-999-87-00')
customer2 = Customer('Рыбаков', 'Максимилиан', 'Семёнович', '067-399-15-90')
customer3 = Customer('Павлов', 'Оскар', 'Лаврентьевич', '067-981-55-76')
customer4 = Customer('Иванов', 'Остап', 'Петрович', '067-233-21-37')
customer5 = Customer('Красильников', 'Елисей', 'Богданович', '067-268-96-96')

print(customer1)
print(customer2)
print(customer3)
print(customer4)
print(customer5)

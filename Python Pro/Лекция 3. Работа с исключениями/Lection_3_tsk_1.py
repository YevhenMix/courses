class NonPositive(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exc(self):
        return self.message


price = input('Введите стоимость товара в гривнах: ')

try:
    price = int(price)
    if price < 0:
        raise NonPositive('Вы ввели отрицательное число!')

except NonPositive as np:
    print(np.get_exc())

except ValueError:
    print('У вас в тексте присутствуют лишние символы(не цифры)!')

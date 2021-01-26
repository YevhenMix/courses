from datetime import datetime
from time import sleep
# ЗАДАЧА № 1
""" Создайте дескриптор который будет делать поля класса управляемые им, доступными только для чтения. """


class OnlyRead:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError('field only for read')

    def __delete__(self, instance):
        raise AttributeError('field only for read')


class Volkswagen:

    mark = OnlyRead('Volkswagen')
    wheels = OnlyRead(4)
    country = OnlyRead('Germany')

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'Mark: {self.mark}\nModel: {self.model}\nCountry: {self.country}\nWheels: {self.wheels}'


polo = Volkswagen('Polo')

print(polo.mark)
print(polo.model)
polo.model = 'CC'
print(polo.model)
polo.mark = 'Mercedes'


# ЗАДАЧА № 2
'''Реализуйте функционал который будет запрещать установку полей класса любыми значениями, кроме целых чисел. Т.е. 
если тому или иному полю попытаться присвоить например строку, то должно быть возбужденно исключение.'''


class OnlyInt:

    def __init__(self, value: int):
        self.chek_value(value)

    def chek_value(self, value):
        if type(value) is int:
            self.value = value
        else:
            raise AttributeError('set only int')

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.chek_value(value)


class Diary:

    math = OnlyInt(5)
    geo = OnlyInt(2)


vlad = Diary()

print(vlad.math)
print(vlad.geo)
vlad.math = 1
print(vlad.math)
vlad.geo = '2'

# ЗАДАЧА № 3
'''Реализуйте свойство класса, которое обладает следующим функционалом: при установки значения этого свойства, в файл 
с заранее определенным названием должно сохранятся время (когда устанавливали значение свойства) и 
установленное значение.'''


class Button:

    def __init__(self, file_name, active=0):
        self.__active = active
        self.file_name = file_name

    def get_state(self):
        return self.__active

    def set_state(self, value):
        self.__active = value
        with open(f'{self.file_name}.txt', 'a') as file:
            text = f'{datetime.now()} -> {self.active}\n'
            file.writelines(text)

    active = property(get_state, set_state)

    def __str__(self):
        return f'State: {self.active}'


big_red_button = Button('BRB', 0)
reactor = Button('Stop', 1)

for i in range(1, 10):
    print(big_red_button)
    big_red_button.active = i
    sleep(1)

for i in range(15):
    print(reactor)
    reactor.active = i
    sleep(1)

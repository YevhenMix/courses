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

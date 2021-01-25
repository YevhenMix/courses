class AddToStr:
    def __init__(self, text):
        self.text = text

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return f'{self.text} {func(*args, **kwargs)}'
        return wrapper


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @AddToStr("I'm say")
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age} years'


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @AddToStr('Hi')
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age} years'


class Mouse:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @AddToStr('Hello')
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age} years'


cat = Cat('Asy', 3)
dog = Dog('Aleks', 2)
mouse = Mouse('Ramie', 5)

print(cat)
print(dog)
print(mouse)

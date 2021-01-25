def add_to_str(text):
    def inner(cls):
        def wrapper(*args, **kwargs):
            cls.text = text
            return cls(*args, **kwargs)
        return wrapper
    return inner


class AddToStr:
    def __init__(self, text):
        self.text = text

    def __call__(self, cls):
        def wrapper(*args, **kwargs):
            cls.text = self.text
            return cls(*args, **kwargs)
        return wrapper


@add_to_str('My ')
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.text + f'Name: {self.name}, Age: {self.age} years'

    def name_only(self):
        return self.name


@AddToStr('Hi ')
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.text + f'Name: {self.name}, Age: {self.age} years'

    def name_only(self):
        return self.name


@add_to_str('Hello ')
class Mouse:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.text + f'Name: {self.name}, Age: {self.age} years'

    def name_only(self):
        return self.name


cat = Cat('Asy', 3)
dog = Dog('Aleks', 2)
mouse = Mouse('Ramie', 5)

print(cat)
print(cat.name_only())
print(dog)
print(dog.name_only())
print(mouse)
print(mouse.name_only())

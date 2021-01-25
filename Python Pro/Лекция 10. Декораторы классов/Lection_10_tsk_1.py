cls_lst_from_cls = []
cls_lst_from_func = []


class AddClsToLst:
    def __init__(self, cls):
        self.cls = cls
        cls_lst_from_cls.append(cls)

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)


def add_cls_to_lst(cls):
    cls_lst_from_func.append(cls)

    def wrapper(*args, **kwargs):
        return cls(*args, **kwargs)
    return wrapper


@add_cls_to_lst
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age} years'


@AddClsToLst
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age} years'


@AddClsToLst
class Mouse:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age} years'


@add_cls_to_lst
class Bee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age} years'


print(cls_lst_from_cls)
print(cls_lst_from_func)

cat = Cat('Asy', 3)
dog = Dog('Aleks', 2)
mouse = Mouse('Ramie', 5)
bee = Bee('Oscar', 1)

print(dog)
print(cat)
print(mouse)
print(bee)

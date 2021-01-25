from functools import wraps

'''3) Предположим, в классе определен метод __str__, который возвращает строку на основании класса. Создайте такой 
декоратор для этого метода, чтобы полученная строка сохранялась в текстовый файл, имя которого совпадает с именем 
класса, метод которого вы декорировали. '''


def save_str_to_file(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        name = f.__qualname__.split('.')[0]
        with open(f'{name}.txt', 'a') as file:
            file.writelines(f(*args, **kwargs))
        return f(*args, **kwargs)
    return wrapper


class Cat:

    def __init__(self, breed, gender, color, age):
        self.breed = breed
        self.gender = gender
        self.color = color
        self.age = age

    @save_str_to_file
    def __str__(self):
        return f'Breed: {self.breed}\nGender: {self.gender}\nColor: {self.color}\nAge: {self.age} years\n'


class Dog:

    def __init__(self, breed, gender, color, age):
        self.breed = breed
        self.gender = gender
        self.color = color
        self.age = age

    @save_str_to_file
    def __str__(self):
        return f'Breed: {self.breed}\nGender: {self.gender}\nColor: {self.color}\nAge: {self.age} years\n'


ves = Cat('Lop-eared', 'male', 'Red', '2')
corgi = Dog('Corgi', 'female', 'Gray', '1')

print(ves)
print(corgi)

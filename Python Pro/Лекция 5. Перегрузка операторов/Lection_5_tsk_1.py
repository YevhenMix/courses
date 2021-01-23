"""1) Создайте класс  «Прямоугольник», у которого присутствуют два поля (ширина и высота). Реализуйте метод сравнения
прямоугольников по площади. Также реализуйте методы сложения прямоугольников (площадь суммарного прямоугольника должна
быть равна сумме площадей прямоугольников, которые вы складываете). Реализуйте методы умножения прямоугольника на число
n (это должно увеличить площадь базового прямоугольника в n раз)"""
from random import randint


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def find_area(rectangle):
        return rectangle.height * rectangle.width

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.find_area(self) == self.find_area(other)
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Rectangle):
            return not self.find_area(self) == self.find_area(other)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.find_area(self) > self.find_area(other)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.find_area(self) < self.find_area(other)
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.find_area(self) >= self.find_area(other)
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.find_area(self) <= self.find_area(other)
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            area = self.find_area(self) + self.find_area(other)
            side_a = self.width + (other.width / 2)
            side_b = area / side_a
            return Rectangle(side_a, side_b)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Rectangle):
            area = self.find_area(self) + self.find_area(other)
            side_a = self.width + (other.width / 2)
            side_b = area / side_a
            return Rectangle(side_a, side_b)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Rectangle(self.width*other, self.height)
        else:
            return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            return Rectangle(self.width * other, self.height)
        else:
            return NotImplemented


a = Rectangle(randint(1, 9), randint(1, 9))
b = Rectangle(randint(1, 9), randint(1, 9))

c = a + b
a += b

print(c.find_area(c))
print(a.find_area(a))

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

c = b * 2
d = b * 3
print(c.height, c.width, c.find_area(c))
print(d.height, d.width, d.find_area(d))

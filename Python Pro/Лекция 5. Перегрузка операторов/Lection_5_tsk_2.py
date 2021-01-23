"""2) Создайте класс «Правильная дробь» и реализуйте методы сравнения, сложения, вычитания и произведения для
экземпляров этого класса."""
from math import gcd
from random import randint


class ProperFraction:

    def __init__(self, nominator, denominator, part=None):
        if nominator < denominator:
            self.nominator = nominator
            self.denominator = denominator
            self.part = part
        else:
            raise ValueError(f'Вы ввели неправильную дробь! Необходимо числитель < знаменателя')

    @staticmethod
    def count_division(fraction):
        return fraction.nominator / fraction.denominator

    @staticmethod
    def lcm(a, b):
        return (a * b) // gcd(a, b)

    @staticmethod
    def whole_part(nominator, denominator):
        i = 0
        while True:
            if not nominator % denominator:
                part = nominator // denominator
                return part, i, denominator
            i += 1
            nominator -= 1

    def count_dop_mul(self, other):
        lowest_cr = self.lcm(self.denominator, other.denominator)
        dop_mul1 = lowest_cr / self.denominator
        dop_mul2 = lowest_cr / other.denominator
        return dop_mul1, dop_mul2, lowest_cr

    def __eq__(self, other):
        if isinstance(other, ProperFraction):
            return self.count_division(self) == self.count_division(other)
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ProperFraction):
            return not self.count_division(self) == self.count_division(other)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, ProperFraction):
            return self.count_division(self) > self.count_division(other)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, ProperFraction):
            return self.count_division(self) < self.count_division(other)
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, ProperFraction):
            return self.count_division(self) >= self.count_division(other)
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, ProperFraction):
            return self.count_division(self) <= self.count_division(other)
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, ProperFraction):
            tmp = self.count_dop_mul(other)
            nominator = (self.nominator * tmp[0]) + (other.nominator * tmp[1])
            try:
                return ProperFraction(nominator, tmp[2])
            except ValueError:
                lst = self.whole_part(nominator, tmp[2])
                return ProperFraction(lst[1], lst[2], lst[0])
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, ProperFraction):
            tmp = self.count_dop_mul(other)
            nominator = (self.nominator * tmp[0]) + (other.nominator * tmp[1])
            try:
                return ProperFraction(nominator, tmp[2])
            except ValueError:
                lst = self.whole_part(nominator, tmp[2])
                return ProperFraction(lst[1], lst[2], lst[0])
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ProperFraction):
            tmp = self.count_dop_mul(other)
            nominator = (self.nominator * tmp[0]) - (other.nominator * tmp[1])
            try:
                return ProperFraction(nominator, tmp[2])
            except ValueError:
                lst = self.whole_part(nominator, tmp[2])
                return ProperFraction(lst[1], lst[2], lst[0])
        else:
            return NotImplemented

    def __isub__(self, other):
        if isinstance(other, ProperFraction):
            tmp = self.count_dop_mul(other)
            nominator = (self.nominator * tmp[0]) - (other.nominator * tmp[1])
            try:
                return ProperFraction(nominator, tmp[2])
            except ValueError:
                lst = self.whole_part(nominator, tmp[2])
                return ProperFraction(lst[1], lst[2], lst[0])
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, ProperFraction):
            return ProperFraction(self.nominator * other.nominator, self.denominator * other.denominator)
        else:
            return NotImplemented

    def __str__(self):
        if self.part:
            return f'Fraction:{self.part}({self.nominator} / {self.denominator})'
        else:
            return f'Fraction:{self.nominator} / {self.denominator}'


first = ProperFraction(randint(1, 10), randint(10, 26))
second = ProperFraction(randint(1, 10), randint(1, 10))

print(first)
print(second)

plus = first + second
minus = first - second
mul = first * second

print(plus)
print(minus)
print(mul)

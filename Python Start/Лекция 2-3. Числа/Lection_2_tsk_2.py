from math import sqrt

print('Программа вычисляет площадь треугольника по сторонам.')

a = float(input('Введите сторону a: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону c: '))

p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))   # или без math (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)

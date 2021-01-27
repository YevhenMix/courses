print('Программа разбивает 5-ти значное число на цифры из которого оно состоит.')

# решение когда сразу int

num = int(input('Введите желаемое число: '))

first = num // 10000
second = num % 10000 // 1000
third = num % 1000 // 100
fourth = num % 100 // 10
fifth = num % 10

print(first)
print(second)
print(third)
print(fourth)
print(fifth)

# строковый вариант с помощью функции map
a, b, c, d, e = map(int, input())
print(a)
print(b)
print(c)
print(d)
print(e)

# через генератор
a, b, c, d, e = (int(i) for i in input())
print(a)
print(b)
print(c)
print(d)
print(e)

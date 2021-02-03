from random import randint

print('Программа разворачивает список без срезов и без дополнителных списокв')

a = [randint(1, 10) for i in range(randint(2, 10))]

print(a)

for i in range(len(a)):
    el = a.pop()
    a.insert(i, el)

print(a)

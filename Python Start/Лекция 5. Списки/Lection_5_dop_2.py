from random import randint

'''Есть массив, в котором последний элемент должен стать первым.
Пустой список или список только с одним элементом должен остаться прежними'''

lst = [randint(0, 5) for i in range(randint(0, 10))]

print(lst)

if lst:
    lst.insert(0, lst.pop())

print(lst)


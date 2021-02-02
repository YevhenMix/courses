from random import randint

'''Создайте список случайных чисел, со случайным количестом элементов от 3 до 10.
Ваше задача -  из списка вернуть набор с 3 элементами -
 первым, третьим, вторым с конца.'''

lst = [randint(0, 15) for i in range(randint(3, 10))]

print(lst)

lst2 = [lst[0], lst[2], lst[-2]]

print(lst2)

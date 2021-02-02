from random import randint

'''Есть массив, который необходимо разделить на два.
Если в нем нечетное количество элементов, то в первом массиве должно быть больше элементов.
Если у него нет элементов, то должны быть возвращены два пустых массива.'''

lst = [randint(0, 10) for i in range(randint(0, 10))]

print(len(lst))

if len(lst) % 2:
    print(lst)
    mat = [lst[:(len(lst) // 2)+1], lst[(len(lst) // 2)+1:]]
    print(mat)
else:
    print(lst)
    mat = [lst[:len(lst) // 2], lst[len(lst) // 2:]]
    print(mat)

print('Программа считает нечетные числа в списке')

lst = [0, 5, 2, 4, 7, 1, 3, 19]

odd = 0
for el in lst:
    if el % 2:  # или el % 2 != 0
        odd += 1

print(odd)

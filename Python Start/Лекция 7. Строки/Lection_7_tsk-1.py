print("Программа считает количество букв 'b' в введенной строке")

# простое решение
st = input('Введите строку: ')

print(st.count('b'))

# решение через циклы

tmp = 0
for el in st:
    if el == 'b':
        tmp += 1
print(tmp)



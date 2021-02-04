print('Программа определяет самое длинное слово из введенных')

st = [i for i in input('Введите слова: ').split()]

long = ''

for el in st:
    if len(el) > len(long):
        long = el

print(long)

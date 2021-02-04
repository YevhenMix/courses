print('Программа проверяет имя на валидность')

name = input('Введите ваше имя: ')

if name.istitle() and name.isalpha():
    print('Имя валидно!')


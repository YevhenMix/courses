print('Программа рисует прямоугольник по вашим параметрам')

width = int(input('Введите ширину прямоугольника: '))
height = int(input('Введите высоту прямоугольника: '))

for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1:
            print('*', end='')
        else:
            print('*', ' ' * (width - 4), '*', end='')
            break
    print()

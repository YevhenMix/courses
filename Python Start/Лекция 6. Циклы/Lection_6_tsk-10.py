print('Программа рисует песочные часы по вашей ширине')

a = int(input('Введите нечетное число: '))

while True:
    if a % 2 == 0:
        a = int(input('Вы ввели четное число! Введите нечетное число: '))
    else:
        break

for i in range(int(a/2)+1):
    for j in range(i):
        print(' ', end=' ')

    for j in range(a-i*2):
        print('*', end=' ')
    print()

for i in range(int(a/2)):
    for j in range(1, int(a/2)-i):
        print(' ', end=' ')

    for j in range(1, 4+i*2):
        print('*', end=' ')
    print()


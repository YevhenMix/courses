print('Программа высчитывает факториал')

f = int(input('Введите число факториал которого вы хотите узнать: '))

ans = 1

for i in range(1, f + 1):
    ans *= i

print(ans)

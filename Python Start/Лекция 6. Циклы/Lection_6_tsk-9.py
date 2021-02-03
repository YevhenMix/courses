print('Программа выводит простые числа от 1 до 100')

for num in range(2, 101):
    pr = True
    for div in range(2, num):
        if num % div == 0:
            pr = False
    if pr:
        print(num)

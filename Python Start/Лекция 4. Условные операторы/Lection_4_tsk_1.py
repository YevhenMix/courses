print('Программа выводит наибольшее число из заданых.')

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))
d = float(input('Введите четвертое число: '))

# простое решение с встроенной функцией max

print(max(a, b, c, d))

# без списков

if a >= b and a >= c and a >= d:
    print(a)
elif b >= a and b >= c and b >= d:
    print(b)
elif c >= a and c >= b and c >= d:
    print(c)
else:
    print(d)

# с помощью all

if all([a >= b, a >= c, a >= d]):
    print(a)
elif all([b >= a, b >= c, b >= d]):
    print(b)
elif all([c >= a, c >= b, c >= d]):
    print(c)
else:
    print(d)




from random import randint


def my_filter(sequence, func):
    final = []
    for el in sequence:
        final.append(func(el))
    return sum(final)


f = [lambda x: x * 2, lambda x: x ** 3, lambda x: x / 2, lambda x: x // 4, lambda x: x + 10]
lst = [randint(2, 50) for i in range(randint(2, 10))]

print(lst)

for i in range(len(f)):
    print(f'{i+1}) Function result: {my_filter(lst, f[i])}')

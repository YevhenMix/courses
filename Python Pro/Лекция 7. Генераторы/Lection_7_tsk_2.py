from random import randint


def my_range(*args):
    if len(args) == 1:
        stop = args[0]
        i = 0
        while i != stop:
            yield i
            i += 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        if start > stop:
            return []
        else:
            while start != stop:
                yield start
                start += 1
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
        if start > stop:
            return []
        else:
            while start < stop:
                yield start
                start += step
    else:
        raise TypeError


for col in range(5):
    stop1 = randint(1, 30)
    print(f'{stop1}')
    a = range(stop1)
    b = my_range(stop1)
    print(f'Classic range: {list(a)}')
    print(f'My range: {list(b)}')

print('*' * 100)

for col in range(5):
    start1 = randint(1, 30)
    stop1 = randint(1, 30)
    print(f'{start1}, {stop1}')
    a = range(start1, stop1)
    b = my_range(start1, stop1)
    print(f'Classic range: {list(a)}')
    print(f'My range: {list(b)}')

print('*' * 100)

for col in range(5):
    start1 = randint(1, 30)
    stop1 = randint(1, 30)
    step1 = randint(1, 5)
    print(f'{start1}, {stop1}, {step1}')
    a = range(start1, stop1, step1)
    b = my_range(start1, stop1, step1)
    print(f'Classic range: {list(a)}')
    print(f'My range: {list(b)}')


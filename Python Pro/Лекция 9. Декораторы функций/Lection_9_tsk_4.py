import time

'''4) Создайте декоратор с параметрами для проведения хронометража работы той или иной функции. Параметрами должны 
выступать то, сколько раз нужно запустить декорируемую функцию и в какой файл сохранить результаты хронометража. Цель - 
провести хронометраж декорируемой функции.'''


def count_timing(h_m, name):
    def inner(f):
        def wrapper(*args, **kwargs):
            with open(f'{name}.txt', 'w') as file:
                all_start = time.time()
                for i in range(h_m):
                    start = time.time()
                    f(*args, **kwargs)
                    stroka = f'{i+1}) Time func -> {time.time() - start} sec.\n'
                    file.write(stroka)
                file.write(f'Full Timing: {time.time() - all_start}')
            return f(*args, **kwargs)
        return wrapper
    return inner


@count_timing(10, 'lst')
def create_lst(size):
    return [i for i in range(size)]


@count_timing(10, 'gen')
def create_lst_gen(size):
    return list((i for i in range(size)))


print(create_lst(500000))
print(create_lst_gen(500000))

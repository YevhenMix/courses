'''2) Создайте декоратор, который зарегистрирует декорируемую функцию в списке функций, для обработки
последовательности.'''

func_lst = []


def add_to_func_lst(f):
    func_lst.append(f)
    return f


@add_to_func_lst
def sum_2(a, b):
    return a + b


@add_to_func_lst
def minus_2(a, b):
    return a - b


def mul_2(a, b):
    return a * b


print(func_lst)

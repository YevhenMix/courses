from functools import wraps

"""1) Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция."""


class CountingCall:

    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f'Counting func({self.f.__name__}) from class: {self.count}')
        return self.f(*args, **kwargs)


def counting_call(f):
    count = 0

    @wraps(f)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Counting func({f.__name__}) from function: {count}')
        return f(*args, **kwargs)
    return wrapper


@CountingCall
@counting_call
def sum_2(a, b):
    return a + b


@CountingCall
@counting_call
def minus_2(a, b):
    return a - b


print(sum_2(2, 2))
print(sum_2(2, 3))
print(sum_2(2, 4))
print(minus_2(4, 1))
print(minus_2(4, 2))
print(sum_2(10, 12))

func = sum_2

print(func(3, 3))

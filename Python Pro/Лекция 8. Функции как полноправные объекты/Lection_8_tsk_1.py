from random import randint


def variable_sequence(start, size, func):
    try:
        for col in range(size):
            tmp = yield start
            if tmp is not None:
                func = tmp
            start = func(start)
    except Exception:
        return


fn = [lambda x: x * 3, lambda x: x / 2, lambda x: x + 5, lambda x: x - 10]

start1, size1 = randint(1, 6), randint(10, 20)
print(start1, size1)

for f in fn:
    for i in variable_sequence(start1, size1, f):
        print(i)
    print('*' * 500)

gn = variable_sequence(1, 20, fn[0])

print(next(gn))
print(next(gn))
print(next(gn))
print(gn.send(fn[2]))
print(next(gn))
print(next(gn))
print(gn.send(fn[1]))
print(next(gn))
try:
    gn.throw(Exception)
except StopIteration:
    pass

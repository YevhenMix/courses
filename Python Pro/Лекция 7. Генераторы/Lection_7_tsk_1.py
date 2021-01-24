from random import randint


def geometric_progression(num, stop):
    sled = 1 * num
    try:
        while sled < stop:
            yield sled
            sled *= num
    except Exception:
        return


def geometric_progression_second(stop):
    num = 2
    sled = 1 * num
    try:
        while sled < stop:
            tmp = yield sled
            if tmp is not None:
                num = tmp
            sled *= num
    except Exception:
        return


pr = geometric_progression_second(randint(100, 1000))

print(next(pr))
print(next(pr))
print(pr.send(3))
print(next(pr))
print(next(pr))
try:
    pr.throw(Exception)
except StopIteration:
    pass

prog = geometric_progression(randint(3, 5), randint(100, 1000))
for i in prog:
    print(i)
    if i > 100:
        prog.throw(Exception)

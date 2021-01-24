from random import randint


def prime_num(num):
    lst = []
    for i in range(2, num + 1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
            yield i


for n in prime_num(randint(1, 500)):
    print(n)

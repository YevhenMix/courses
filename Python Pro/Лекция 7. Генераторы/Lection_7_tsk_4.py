from random import randint

gen = (i ** 3 for i in range(2, randint(3, 20)+1))

print(list(gen))

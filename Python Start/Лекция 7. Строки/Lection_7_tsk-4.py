from math import pi

'''Выведите на экран 10 строк со значением числа Pi. В первой строке должно быть 2 знака после запятой, во второй 3 
и так далее. '''

for inu in range(2, 12):
    tmp = '{:.' + str(inu) + 'f}'
    print(tmp.format(pi))

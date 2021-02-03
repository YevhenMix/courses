from random import randint

print('Программа считает среднюю зарплату сотрудника')

salary = [randint(7500, 15000) for i in range(12)]

print(salary)

average = sum(salary) / len(salary)

print(average)

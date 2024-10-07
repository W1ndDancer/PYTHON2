'''
from math import sqrt

a, b, c = 5, -10, -400
d = b**2 - 4*a*c
print(f'D = {d}')

if d > 0:
    x1 = (-b + sqrt(d))/(2*a)
    x2 = (-b - sqrt(d))/(2*a)
    print(f'x1 = {x1} /n x2 = {x2}')
elif d == 0:
    x = -b/(2*a)
    print(f'x={x}')
else:
    print('no roots')
'''

# Задание №5
# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

'''
n = 20
e = 3
sum_num = 0
number = 0

while number <= n:
    number += 1
    if number % 2 == 0:
        if number % e == 0:
            continue
        sum_num += number
print(f'sum = {sum_num}')
'''

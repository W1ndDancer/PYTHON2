# Задание №1
# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

# a = 10
# b = 10.5
# c = 'test'
# d = [a, b]
# e = {'test': a}

# print(f'объект {a} имеет тип {type(a)}')
# print(f'объект {b} имеет тип {type(b)}')
# print(f'объект {c} имеет тип {type(c)}')
# print(f'объект {d} имеет тип {type(d)}')
# print(f'объект {e} имеет тип {type(e)}')

# Задание №2
# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите: порядковый номер начиная с единицы
# значение адрес в памяти размер в памяти хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

# import sys

# data = [42, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!']
# for n, item in enumerate(data, 1):
#     check_int = "Число является целым" if isinstance(item, int) else ""
#     check_str = "Это строка" if isinstance(item, str) else ""
#     print(f'{n}. Объект {item}\nАдрес: {id(item)}\tРазмер: {sys.getsizeof(item)}\t'
#     f'Хэш: {hash(item)} {check_int}{check_str}')

# Задание №4 Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру. Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять не менее 42 знаков после запятой

# import math
# import decimal

# decimal.getcontext().prec = 50
# PI = decimal.Decimal(math.pi)

# d = decimal.Decimal(input('Введите диаметр: '))
# while d > 1000:
#     print('Введено число вне диапазона, больше 1000')
#     d = decimal.Decimal(input('Введите диаметр: '))

# decimal.Decimal
# s = PI * (d/2) ** 2
# l = PI * d

# print(f'S = {s}\nL = {l}')

# Задание №5 Напишите программу, которая решает квадратные уравнения даже если
# дискриминант отрицательный.
# Используйте комплексные числа
# для извлечения квадратного корня.

# a = float(input('Введите коэффициент a = '))
# b = float(input('Введите коэффициент b = '))
# c = float(input('Введите коэффициент c = '))

# d = b ** 2 - 4 * a * c

# if d > 0:
#     x1 = (- b + d ** 0.5) / (2 * a)
#     x2 = (- b - d ** 0.5) / (2 * a)
#     res = f'У уравнения два корня: {x1 = } и {x2 = }'
# elif d == 0:
#     x = - b / (2 * a)
#     res = f'У уравнения один корень: {x = }'
# else:
#     d = complex(d, 0)
# print(d)
# x1 = (- b + d ** 0.5) / (2 * a)
# x2 = (- b - d ** 0.5) / (2 * a)
# res = f'У уравнения два комплексных корня: {x1 = } и {x2 = }'

# print(res)

# Задание №6 Напишите программу банкомат. 
# Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е. Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%. Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
# Любое действие выводит сумму денег

import decimal

CMD_WITHDRAW = "с"
CMD_DEPOSIT = "п"
CMD_EXIT = "в"
MULTIPLICITY = 50
NUMBER_OPERATION = 3
PRECENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(5_000_000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PRECENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)

balance = decimal.Decimal(60000000)
count = 0

while True:
    action = input(f"Пополнить - '{CMD_DEPOSIT}', снять - '{CMD_WITHDRAW}', выйти - '{CMD_EXIT}' ")
    if action == CMD_EXIT:
        print(f"Заберите карту. баланс:{balance}у.е")
        break
    if balance > RICHNESS_SUM:
        percent = balance * RICHNESS_PERCENT
        balance -= percent
        print(f"Вычтен налог на богатство {RICHNESS_PERCENT * 100}%. "
        f"Сумма процента - {percent}. Баланс карты - {balance}")

    if action in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
    while amount % MULTIPLICITY != 0:
        amount = decimal.Decimal(input(f"Введите сумму кратнную {MULTIPLICITY}: "))

    if action == CMD_DEPOSIT:
        count += 1
        balance+=amount
        print(f"Пополнение карты на {amount}. Баланс карты: {balance}")
    elif action == CMD_WITHDRAW:
        percent=amount*PRECENT_REMOVAL
        percent= MIN_REMOVAL if percent<MIN_REMOVAL else MAX_REMOVAL if percent>MAX_REMOVAL else percent
        sub=amount+percent
        if balance>sub:
            balance-=sub
            count+=1
            print(f"Снятие с карты {amount}у.е. Сумма процента за снятие {percent}. "
            f"Баланс карты {balance}")
    else:
        print(f"Недостаточно средств. Сумма снятия {amount}. Сумма процента за снятие {percent}."
        f"Баланс карты {balance}")
        if count%NUMBER_OPERATION==0:
            bonus = balance * PRECENT_BONUS
            balance+=bonus
            print(f"Начислен бонус: {bonus} за каждую {NUMBER_OPERATION}. Баланс карты {balance}")
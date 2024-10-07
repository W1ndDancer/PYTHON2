# 1. Проверить год на високосность

# REFORM = 1582
# BIG_LEAP_YEAR = 400
# SMALL_LEAP_YEAR = 4
# LARGE_NON_LEAP_YEAR = 100
# ZERO = 0
# year = int(input('Введите год в формате yyyy: '))
# result = ''

# if REFORM > year:
#     result = 'Не ввели календарь'
# elif year % SMALL_LEAP_YEAR != 0 or year % LARGE_NON_LEAP_YEAR == 0 and year % BIG_LEAP_YEAR != 0:
#     result = "Обычный"
# else:
#     result = "Високосный"
# print(result)

# 2. Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

# MIN = 1
# MAX = 999
# ONE = 1
# TEN = 10
# HUNGREED = 100

# num = 0
# while num < MIN or num > MAX:
#     num = int(input(f'Input a number between {MIN} and {MAX}\n'))
# if num < TEN:
#     result = f'{num} is a one-digit number, square of {num} is {num*num}'
# elif num < HUNGREED:
#     prod = (num // TEN) * (num % TEN)
#     result = f'{num} is a two-digit number, product of digits is {prod}'
# else:
#     mirror = int(f'{num % TEN}{num // TEN % TEN}{num // HUNGREED}')
#     result = f'{num} is a three-digit number, mirror of number is {mirror}'
# print(result)

# 3. Нарисовать елку в консоли

# SPACE = ' '
# STAR = '*'
# rows = int(input('how much rows? '))
# spaces = rows - 1
# stars = 1

# for _ in range(rows):
#     print(spaces * SPACE + stars * STAR)
#     stars += 2
#     spaces -= 1

# 4. Вывести таблицу умножения. Как в школьной тетрадке
SPACES = '     '
print()
for i in range(2,11):
    for j in range(2, 6):
        if j < 5:
            print(f'{j} * {i:<2} = {j*i:>2}', end = SPACES)
        else:
            print(f'{j} * {i:<2} = {j*i:>2}')
print()
print()
for i in range(2,11):
    for j in range(6, 10):
        if j < 9:
            print(f'{j} * {i:<2} = {j*i:>2}', end = SPACES)
        else:
            print(f'{j} * {i:<2} = {j*i:>2}')
print()
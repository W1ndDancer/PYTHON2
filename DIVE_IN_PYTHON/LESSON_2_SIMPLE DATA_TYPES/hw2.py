# 1. Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# num = 16

# def convert_to_16(number, upper=True):
#     BASE = 16
#     digits = '0123456789abcdef'
#     result = ''
#     while number > 0:
#         result = digits[number % BASE] + result
#         number //= BASE
#     return result.upper() if upper else result

# res = convert_to_16(num)

# print(f'Шестнадцатеричное представление числа: {res}\nПроверка результата: {hex(num)}')

# 2. На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

# Разбиваем строки на числитель и знаменатель без использования map
numerator1_str, denominator1_str = frac1.split('/')
numerator2_str, denominator2_str = frac2.split('/')

# Преобразуем строки в целые числа
numerator1 = int(numerator1_str)
denominator1 = int(denominator1_str)
numerator2 = int(numerator2_str)
denominator2 = int(denominator2_str)

common_denominator = denominator1 * denominator2

new_numerator1 = numerator1 * denominator2
new_numerator2 = numerator2 * denominator1

summation_numerator = new_numerator1 + new_numerator2
multiplication_numerator = numerator1 * numerator2

print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")

# Преобразуем введенные строки в объекты Fraction

def summation(frac1, frac2):
    return Fraction(int(frac1[0]), int(frac1[2])) + Fraction(int(frac2[0]), int(frac2[2]))

def multiplication(frac1, frac2):
    return Fraction(int(frac1[0]), int(frac1[2])) * Fraction(int(frac2[0]), int(frac2[2]))

print(f"Сумма дробей: {summation(frac1, frac2)}")
print(f"Произведение дробей: {multiplication(frac1, frac2)}")

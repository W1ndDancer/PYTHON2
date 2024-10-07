# 1. Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

# data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
# print(data)
# print(f'Новое множество: {list(set(data))}')
# new_list =[]
# for item in data:
#     if item not in new_list:
#         new_list.append(item)
# print(new_list)

# Задание №2 Пользователь вводит данные. Сделайте проверку данных 
# и преобразуйте если возможно в один из вариантов ниже:
# Целое положительное число
# Вещественное положительное или отрицательное число
# Строку в нижнем регистре, если в строке есть 
# хотя бы одна заглавная буква
# Строку в нижнем регистре в остальных случаях

# data = input('Введите данные: ')

# if data.isdigit():
#     result = int(data)
# elif data.replace(".","").replace("-","").isdigit()\
#     and data.count('.') < 2 and "-" not in data[1:] :
#     result = float(data)
# elif not data.islower():
#     result = data.lower()
# else:
#     result = data.upper()
# print(f'{result= }')

# Задание №3
# Создайте вручную кортеж содержащий элементы разных типов. 
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

# data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)

# result = {}

# for item in data:
#     item_type = type(item)
# if item_type not in result:
#     result[item_type] = [item]
# else:
#     result[item_type].append(item)
# print(result)

# #2

# data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)
# result = {}
# for item in data:
#     item_type = type(item)
# if item_type not in result:
#     result[item_type] = [el for el in data if type(el) == item_type]
# print(result)

# #3

# data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)
# result = {}
# for item in data:
#     key = result.setdefault(type(item), [])
#     key.append(item)
# print(result)

# Задание №4
# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

# data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]

# data = [item for item in data if data.count(item) != 2]

# print(data)

# # data1 = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]

# # unique_list = []

# # for item in data1:
# #     if data.count(item) != 2:
# #         unique_list.append(item)

# # print(unique_list)

# # data2 = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
# # COUNT = 2

# # for item in set(data2):
# #     if data.count(item) == COUNT:
# #         for _ in range(COUNT):
# #             data2.remove(item)
# #         print(f'{data2 = }')

# Задание №5 Создайте вручную список с повторяющимися целыми числами. 
# Сформируйте список с порядковыми номерами 
# нечётных элементов исходного списка. 
# Нумерация начинается с единицы.

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# unique_list = []
#
# for n, item in enumerate(data, 1):
# if item % 2:
# unique_list.append(n)
#
# print(unique_list)
# data1 = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
# new_list = []
# length = len(data1)
# new_list = [i + 1 for i in range(length) if data1[i] % 2]
# print(new_list)

# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного 
# слова был один пробел между ним и номером строки.

# text = sorted(input('Enter a string: ').split())
# # text.sort() Сохранять в переменную не надо
# max_length = 0
# print(text)

# for word in text:
#     word_len = len(word)
#     if max_length < word_len:
#         max_length = word_len

# for nn, word in enumerate(text, 1):
#     print(f'{nn}. {word:>{max_length}}')

# Задание №7
# Пользователь вводит строку текста. 
# Подсчитайте сколько раз встречается 
# каждая буква в строке без использования 
# метода count и с ним. 
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи 
# символа в строке. 
# Обратите внимание на порядок ключей. Объясните почему они совпадают 
# или не совпадают в ваших решениях.

# text = input('Введите текст: ')
# result = {}
# for char in set(text):
#     result[char] = text.count(char)

# print(result)

# text = input('Введите текст: ')
# result = {}
# for char in text:
#     if char not in result:
#         result[char] = 1
#     else:
#         result[char] += 1
# print(result)

# #3
# result2 = {}
# for char in text:
#     result2[char] = result2.get(char, 0)+1

# print(result)

# 8. Три друга взяли вещи в поход. Сформируйте 
# словарь, где ключ — имя друга, а значение — 
# кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного 
# и имя того, у кого данная вещь отсутствует
# Задание №8 Для решения используйте операции 
# с множествами. Код должен расширяться 
# на любое большее количество друзей.

hike = {
'Aaz': ("спички", "спальник", "дрова", "топор"),
'Skeeve': ("спальник", "спички", "вода", "еда"),
'Tananda': ("вода", "спички", "косметичка"),
}

all_things = set()
# all_things.update(*hike.values())
for values in hike.values():
    all_things.update(values)
print(f'Полный список вещей: {all_things = }')

unique = {}
for master_friend, master_things in hike.items():
    for slave_friend, slave_things in hike.items():
        if master_friend != slave_friend:
            if master_friend not in unique:
                unique[master_friend] = set(master_things) - set(slave_things)
            else:
                unique[master_friend] -= set(slave_things)

print(f'Уникальные вещи: {unique = }')


dublicates = set(all_things)

# uniq_things = set()
# uniq_things.update(*unique.values())
# print(uniq_things)
# dublicates -= uniq_things
# print(dublicates)


for things in unique.values():
    dublicates -= things
print(f'Дублирующиеся вещи: {dublicates = }')

for friend, things in hike.items():
    no_things = dublicates - set(things)
    if no_things:
        print(f'У {friend} отсутствует {no_things}')



# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.

import os
import re
from functools import reduce
os.system("cls")


# 1.
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
#     Пример:
#     - 6782 -> 23
#     - 0,56 -> 11

print('\nЗадача 1')
number = '6782'

lst = list(number.split('.'))
summ = 0
for i in lst:
    for j in i:
        summ += int(j)
print(f"Вариант 1: Сумма цифр вещественного числа равна = {summ}")

# # улучшение
my_sum = sum(map(int, number.replace('.', '')))
print(f"Вариант 2: Сумма цифр = {my_sum}")

# # улучшение
my_sum = reduce(lambda x, y: x + y, [int(i) for i in number])
print('Вариант 3: Сумма =', my_sum)

# 2.
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

print('\nЗадача 2')
n = 4

solving = [1]

solving.extend(solving[i - 2] * i for i in range(2, n + 1))
print('Вариант 1:', solving)

# стало

print('Вариант 2:', [1] + [solving[i - 2] * i for i in range(2, n + 1)])

# 3
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д
#     Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]


print('\nЗадача 3')
source_list = [2, 3, 4, 5, 6]

# # было
counting_pairs1 = 0
counting_pairs1 = (
    len(source_list) // 2 + 1
    if len(source_list) % 2 != 0
    else len(source_list) // 2
)
new_list1 = [source_list[i]*source_list[-i-1] for i in range(counting_pairs1)]
print(f'Вариант 1: {source_list} = > {new_list1}')

# # стало
counting_pairs2 = len(source_list) // 2 + \
    1 if len(source_list) % 2 != 0 else len(source_list)//2
new_list2 = [source_list[i] *
             source_list[len(source_list)-i-1] for i in range(counting_pairs2)]
print(f'Вариант 2: {source_list} = > {new_list2}')

# 4
# # Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# # максимальным и минимальным значением дробной части элементов
# #     Пример:
# #      - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


print('\nЗадача 4')
source_list = [1.1, 1.2, 3.1, 5, 10.01]

new_list = [round(i % 1, 2) for i in source_list if i % 1 != 0]
print(f'Вариант 2: {source_list} = > {max(new_list) - min(new_list)}')

# стало
new_list = [round(i % 1, 2) for i in source_list if i % 1 != 0]
print(f'Вариант 2: {source_list} = > {max(new_list) - min(new_list)}')


# 5
# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
print('\nЗадача 5')
my_text = 'ываабв лповап абвцукв алоабвабв ываываыв'


my_list = my_text.split()
new_list = [x for x in my_list if not re.search('абв', x)]
new_text = " ".join(new_list)
print('Вариант 1:', new_text)

# # стало
my_text = filter(lambda x: 'абв' not in x, my_text.split())
new_text = " ".join(my_text)
print('Вариант 2:', new_text)

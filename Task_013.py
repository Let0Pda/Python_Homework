# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов
#     Пример:
#      - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
os.system("cls")

source_list = [1.1, 1.2, 3.1, 5, 10.01]
# new_list = [round(i % 1, 2) for i in source_list if i % 1 != 0]
# print(f'{source_list} = > {max(new_list) - min(new_list)}')

###
new_list = []
for i in source_list:
    if i % 1 != 0:
        new_list.append(round(i % 1, 2))
print(f'{source_list} = > {max(new_list) - min(new_list)}')


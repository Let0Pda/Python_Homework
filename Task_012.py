# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д
#     Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

import os
os.system("cls")
# исходный список
source_list = [2, 3, 4, 5, 6]

# вариант 1
counting_pairs1 = 0
if len(source_list) % 2 != 0:
    counting_pairs1 = len(source_list)//2 + 1
else:
    counting_pairs1 = len(source_list)//2
new_list1 = []
for i in range(counting_pairs1):
    new_list1.append(source_list[i]*source_list[-i-1])
print(f'Вариант 1: {source_list} = > {new_list1}')

# вариант 2, можно сократить

counting_pairs2 = len(source_list) // 2 + \
    1 if len(source_list) % 2 != 0 else len(source_list)//2
new_list2 = [source_list[i] *
             source_list[len(source_list)-i-1] for i in range(counting_pairs2)]
print(f'\nВариант 2: {source_list} = > {new_list2}')

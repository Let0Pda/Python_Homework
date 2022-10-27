# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

import os
os.system("cls")

my_list = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"\nИсходный список: {my_list}")
new_list = []
[new_list.append(i) for i in my_list if i not in new_list]
print(f"\nСписок из неповторяющихся элементов: {new_list}")

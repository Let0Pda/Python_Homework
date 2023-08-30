# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

import os
from random import randrange
os.system("cls")


def write_file(number):
    with open('task_009.txt', 'w') as data:
        for _ in range(number):
            data.write(f"{randrange(0, 2*number)}\n")


def read_file():
    with open('task_009.txt', 'r') as data:
        indexs = list(map(int, data.readlines()))
    return indexs


n = int(input("Введите число N: "))
lst_number = list(range(-n, n+1))
write_file(n)
lst_index = read_file()
prod = 1
for i in range(len(lst_index)):
    prod *= lst_number[lst_index[i]]
print(f'\nРезультат:')
print(f'список элементов -> {lst_number}')
print(f'позиции из файла -> {lst_index}')
print(f'произведение элементов -> {prod}\n')

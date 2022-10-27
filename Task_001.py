# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
import os
os.system("cls")
day_number = input('Введи цифру, обозначающую день недели: ')
# Верная защита от ...
while day_number not in ('1', '2', '3', '4', '5', '6', '7'):
    print('\nЭто вообще не день недели!\n')
    day_number = input('Введите номер дня недели = ')
    os.system("cls")
day_number = int(day_number)

if 0 < day_number < 6:
    print(day_number, '-> Этот день не выходной) -> нет')
else:
    print(day_number, '-> Этот день выходной -> да')

# while not day_number.isdigit() and day_number not in range(1, 8): # не верно

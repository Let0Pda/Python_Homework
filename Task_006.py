# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
#     Пример:
#     - 6782 -> 23
#     - 0,56 -> 11
import os
os.system("cls")

number = (input("Введите число: ").replace('-', '0').replace('.', '0'))
while not number.isdigit():
    number = (input("Введите еще раз: ").replace('-', '0').replace('.', '0'))

lst = list(str(number).split('.'))
summ = 0
for i in lst:
    for j in i:
        summ += int(j)
print(f"Сумма цифр вещественного числа равна = {summ}")

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
#     Пример:
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ]
import os
os.system("cls")

n = (input("Введите число N: "))
while not n.isdigit():
    n = (input("Введите еще раз: "))
n = int(n)
solving = [1]
solving.extend(solving[i - 2] * i for i in range(2, n + 1))
print(solving)

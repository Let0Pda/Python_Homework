# Задайте список из n чисел последовательности $(1 +\frac 1 n) ^ n$ и выведите на экран их сумму
#       Пример:
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system("cls")

n = (input("Введите число n: "))
while not n.isdigit():
    n = (input("Введите еще раз: "))
n = int(n)
solving = []
for i in range(1, n + 1):
    solving.append(round((1 + 1/i)**i))
print(f"Полученная сумма последовательности {n}: {solving} -> {sum(solving)}")

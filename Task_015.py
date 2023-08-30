# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
#     Пример:
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

import os
os.system("cls")

# # рекурсия тормозит нещадно после 40
# def fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    first, second = 0, 1
    fibonacci_num = 0
    for _ in range(n):
        fibonacci_num = first + second
        second = first
        first = fibonacci_num
    return fibonacci_num


def negative_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for _ in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


set_number = (input("Введите число: "))
while not set_number.isdigit():
    set_number = (input("Введите еще раз: "))
set_number = int(set_number)
list = [0]
for i in range(1, set_number + 1):
    list.append(fibonacci(i))
    list.insert(0, negative_fibonacci(i))
print(list)

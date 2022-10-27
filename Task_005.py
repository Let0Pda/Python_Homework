# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A(3, 6) B(2, 1) -> 5, 09
# - A(7, -5) B(1, -1) -> 7, 21

import os
os.system("cls")

first_point = list(map(int, input(
    "Введите координаты первой точки x y через пробел: ").split()))
second_point = list(map(int, input(
    "\nВведите координаты второй точки x y через пробел: ").split()))
distance = (((second_point[0] - first_point[0])**2 +
            (second_point[1] - first_point[1])**2) ** (0.5))
print(
    f"\nРасстояние между двумя точками пространства = {round(distance, 3)}\n")

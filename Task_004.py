# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти(x и y).
import os
os.system("cls")
x = int(input('Введите номер четверти от 1 до 4 - '))
if x == 1:
    print('\nx>0 and y>0\n')
elif x == 2:
    print('\nx<0 and y>0\n')
elif x == 3:
    print('\nx<0 and y<0\n')
elif x == 4:
    print('\nx>0 and y<0\n')
else:
    print('\nВведите корректное значение\n')

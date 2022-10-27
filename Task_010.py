# Реализуйте алгоритм перемешивания списка

import os
import random
os.system("cls")

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Исходный список:     ', lst)
for i in range(len(lst)-1, 0, -1):
    j = random.randint(0, i + 1)
    lst[i], lst[j] = lst[j], lst[i]
print('Перемешаный список:  ', lst)

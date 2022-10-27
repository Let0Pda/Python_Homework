# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
import os
os.system("cls")

# 1.


def logic_stat(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)


if (logic_stat(0, 0, 0) and logic_stat(0, 0, 1) and logic_stat(0, 1, 0) and
    logic_stat(0, 1, 1) and logic_stat(1, 0, 0) and logic_stat(1, 0, 1) and
        logic_stat(1, 1, 0) and logic_stat(1, 1, 1)):
    print("Истинно\n")
else:
    print("Ложно\n")

# 2.
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is",
                  not (x or y or z) == (not x and not y and not z))

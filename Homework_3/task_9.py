# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint
c = 5
l = 5
matrix = [[] for _ in range(5)]
column = [[] for __ in range(5)]
min_el = []

for i in matrix:
    for j in range(5):
        i.append(randint(0, 10))

for i in matrix:
    for j in i:
        print(f'{j:4}', end='')
    print()

for i in range(5):
    print("  --", end='')
print()

for i in range(5):
    for j in range(5):
        column[i].append(matrix[j][i])

for i in column:
    min_ex = i[0]
    for q in i:
        if q < min_ex:
            min_ex = q
    min_el.append(min_ex)
    print(f'{min_ex:4}', end='')
print()

print(f'Максимальным эдементом среди минимальных элементов столбцов матрицы является {max(min_el)}')
# Задачу решил для матрицы 5х5. Для матрицы любого другого размера можно в начале задаться переменными с указанием
# количества столбцов и строк и работать с ними.
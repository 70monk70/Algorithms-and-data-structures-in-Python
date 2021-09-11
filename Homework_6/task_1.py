# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и
# разрядность вашей ОС.

# Урок 2, задание 4,
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

import sys
from random import randint


n = 5000
elem = []
for el in range(n):
    num = pow(-1/2, el)
    elem.append(num)
print(f'Сумма элекментов массива {elem} равна {round(sum(elem), 5)}')


# print(sys.getsizeof(elem))

# При n = 5 количество памяти - 120
# При n = 50 количество памяти - 472
# При n = 500 количество памяти - 4216
# При n = 5000 количество памяти - 41880
# В данной реализации программы количество задействованной памяти напрямую зависит от длины списка. Что логично,
# наиболее эффективное использование памяти будет там, где длина списка меньше.


# Урок 3, задание 6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

arr = [randint(-1000, 1000) for el in range(500)]
max_ind = arr.index(max(arr))
min_ind = arr.index(min(arr))

if max_ind < min_ind:
    max_ind = arr.index(min(arr))
    min_ind = arr.index(max(arr))

summ = 0

for el in range(min_ind+1, max_ind):
    summ += arr[el]

print(f'Сумма элементов массива, расположенных между минимальным и максимальным элементами массива {arr} равна {summ}')

# print(sys.getsizeof(arr))
# print(sys.getsizeof(summ))
# print(sys.getsizeof(max_ind))
# print(sys.getsizeof(min_ind))

# Объем памяти, выделяемый под переменные (summ, max_ind, min_ind) в данной программе остается постоянным - 28,
# только для списка он является динамическим и зависит от длинны списка (объем памяти, выделяемый под список
# разной длины соответствует объему памяти из предыдущего задания).

# В целом, анализ выделяемой памяти для программ из первых трех уроков, в моем случае, достаточно спорное решение,
# поскольку все программы разрабатывались с использованием списков и объявления простых перемнных. Поэтому и
# выделяемая под эти задачи память зависит для обычных переменных является постоянной, а для списков - динамической и
# зависит только от длины этого списка.
# Python 3.9.0, ОС - Windows 10 x64.

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint

arr = [randint(0, 100) for el in range(10)]
max_ind = arr.index(max(arr))
min_ind = arr.index(min(arr))

if max_ind < min_ind:
    max_ind = arr.index(min(arr))
    min_ind = arr.index(max(arr))

summ = 0

for el in range(min_ind+1, max_ind):
    summ += arr[el]

print(f'Сумма элементов массива, расположенных между минимальным и максимальным элементами массива {arr} равна {summ}')

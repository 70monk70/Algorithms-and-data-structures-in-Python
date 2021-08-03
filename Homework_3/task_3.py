# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

a = int(input('Введите количество элементов массива: '))
arr = [randint(0, 100) for el in range(a)]
print(f'Исходный массив {arr}')
min_arr = min(arr)
max_arr = max(arr)
ind_max = arr.index(max(arr))
ind_min = arr.index(min(arr))
arr[ind_max] = min_arr
arr[ind_min] = max_arr
print(f'Поменяем максимальный и минимальный элементы местами: {arr}')

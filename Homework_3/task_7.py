# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

from random import randint

arr = [randint(0, 100) for el in range(10)]

min_1 = min(arr)
min_1_ind = arr.index(min_1)
arr.remove(min_1)
min_2 = min(arr)
arr.insert(min_1_ind, min_1)


print(f'В массиве {arr} минимальными являются числа {min_1} и {min_2}')
# Определить, какое число в массиве встречается чаще всего
from random import randint

arr = [randint(0, 5) for el in range(10)]
arr_ind = [arr.count(el) for el in arr]
print(f'В массиве {arr}\n'
       f'Чаще всего встречается число {arr[arr_ind.index(max(arr_ind))]} - {max(arr_ind)} раз')
#Ситуацию, когда в массиве несколько чисел встречаются максимально одинаковое количество раз описывать не стал,
# поскольку не до конца понял, как это можно реализовать.
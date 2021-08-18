# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import uniform


def merge_sort(lst):
    if len(lst) == 1 or len(lst) == 0:
        return
    left = lst[:(len(lst) // 2)]
    right = lst[(len(lst) // 2):]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    res = [0] * (len(left) + len(right))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        res[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        res[k] = right[j]
        j += 1
        k += 1
    for i in range(len(lst)):
        lst[i] = res[i]
    return lst


A = [round(uniform(0, 50), 2) for _ in range(10)]
print(f'Исходны список: {A},\n'
      f'Отсортированный список: {merge_sort(A)}.')

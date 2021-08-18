# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
# меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from random import choice
from random import randint


def median(lst, k):
    if len(lst) == 1:
        return lst[0]

    pivot = choice(lst)

    lesser_els = [el for el in lst if el < pivot]
    greater_els = [el for el in lst if el > pivot]
    pivots = [el for el in lst if el == pivot]

    if k < len(lesser_els):
        return median(lesser_els, k)
    elif k < len(lesser_els) + len(pivots):
        return pivots[0]
    else:
        return median(greater_els, k - len(lesser_els) - len(pivots))


M = 5
lst = [randint(0, 50) for _ in range(2 * M + 1)]
print(f'Исходный список: {lst}\n'
      f'Медиана списка: {median(lst, len(lst) / 2)}')
lst.sort()
print(f'Проверка!\n'
      f'Список после сортировки: {lst}\n'
      f'Медиана списка: {lst[len(lst) // 2]}')

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

arr = [randint(-100, 100) for el in range(10)]
negative_numbers = []

for el in arr:
      if el < 0:
            negative_numbers.append(el)

print(f'В массиве {arr}\n'
      f'Максимальный отрицательный элемент - ({max(negative_numbers)}), его позиция - {arr.index(max(negative_numbers))}')

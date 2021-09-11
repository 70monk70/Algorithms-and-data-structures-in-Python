# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания
# первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# В качестве алгоритма выбрал задание № 5 из ДЗ № 3: В массиве найти максимальный отрицательный элемент. Вывести
# на экран его значение и позицию в массиве.
# Для проверки скорости работы алгритма были проверены исходные данные в диапазоне от 10 000 до 100 000 000 для
# каждой реализации (их всего две), поскольку до 10 000 скорость работы была меньше 0.000.

# Мой мысли по поводу скорости и сложности данных методов написаны в самом низу под выходными данными cProfile.

import cProfile
from random import randint


def min_1(n):
    arr = [randint(-100, 100) for _ in range(n)]
    negative_numbers = []
    for el in arr:
        if el < 0:
            negative_numbers.append(el)
    return print(f'Максимальный отрицательный элемент - ({max(negative_numbers)}), его позиция -'
                 f'{arr.index(max(negative_numbers))}')


def min_2(m):
    num_list = [randint(-10, 10) for _ in range(m)]
    min_el = -float('inf')
    for i, item in enumerate(num_list):
        if min_el < item < 0:
            min_el = item
            min_idx = i
            return print(f'Максимальный отрицательный элемент - {min_el}, его позиция {min_idx}')


# cProfile.run('min_1(10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#     10000    0.003    0.000    0.005    0.000 random.py:237(_randbelow_with_getrandbits)
#     10000    0.004    0.000    0.009    0.000 random.py:290(randrange)
#     10000    0.002    0.000    0.011    0.000 random.py:334(randint)
#         1    0.001    0.001    0.014    0.014 task_1.py:12(min_1)
#         1    0.002    0.002    0.013    0.013 task_1.py:13(<listcomp>)
#         1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      4993    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12687    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# cProfile.run('min_2(10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#     10000    0.004    0.000    0.005    0.000 random.py:237(_randbelow_with_getrandbits)
#     10000    0.004    0.000    0.009    0.000 random.py:290(randrange)
#     10000    0.002    0.000    0.012    0.000 random.py:334(randint)
#         1    0.000    0.000    0.014    0.014 task_1.py:22(min_2)
#         1    0.002    0.002    0.013    0.013 task_1.py:23(<listcomp>)
#         1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     15309    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
# cProfile.run('min_1(100000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.139    0.139 <string>:1(<module>)
#    100000    0.033    0.000    0.046    0.000 random.py:237(_randbelow_with_getrandbits)
#    100000    0.041    0.000    0.088    0.000 random.py:290(randrange)
#    100000    0.022    0.000    0.110    0.000 random.py:334(randint)
#         1    0.006    0.006    0.139    0.139 task_1.py:12(min_1)
#         1    0.020    0.020    0.129    0.129 task_1.py:13(<listcomp>)
#         1    0.000    0.000    0.139    0.139 {built-in method builtins.exec}
#         2    0.001    0.000    0.001    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#     49543    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#    100000    0.006    0.000    0.006    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    127584    0.008    0.000    0.008    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# cProfile.run('min_2(100000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.132    0.132 <string>:1(<module>)
#    100000    0.036    0.000    0.050    0.000 random.py:237(_randbelow_with_getrandbits)
#    100000    0.041    0.000    0.091    0.000 random.py:290(randrange)
#    100000    0.022    0.000    0.112    0.000 random.py:334(randint)
#         1    0.000    0.000    0.132    0.132 task_1.py:22(min_2)
#         1    0.020    0.020    0.132    0.132 task_1.py:23(<listcomp>)
#         1    0.000    0.000    0.132    0.132 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#    100000    0.006    0.000    0.006    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    151948    0.009    0.000    0.009    0.000 {method 'getrandbits' of '_random.Random' objects}
# cProfile.run('min_1(1000000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.005    0.005    1.400    1.400 <string>:1(<module>)
#   1000000    0.330    0.000    0.464    0.000 random.py:237(_randbelow_with_getrandbits)
#   1000000    0.409    0.000    0.873    0.000 random.py:290(randrange)
#   1000000    0.218    0.000    1.091    0.000 random.py:334(randint)
#         1    0.061    0.061    1.395    1.395 task_1.py:12(min_1)
#         1    0.206    0.206    1.296    1.296 task_1.py:13(<listcomp>)
#         1    0.000    0.000    1.400    1.400 {built-in method builtins.exec}
#         2    0.007    0.004    0.007    0.004 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#    497855    0.031    0.000    0.031    0.000 {method 'append' of 'list' objects}
#   1000000    0.056    0.000    0.056    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1273870    0.078    0.000    0.078    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# cProfile.run('min_2(1000000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.004    0.004    1.334    1.334 <string>:1(<module>)
#   1000000    0.356    0.000    0.504    0.000 random.py:237(_randbelow_with_getrandbits)
#   1000000    0.404    0.000    0.908    0.000 random.py:290(randrange)
#   1000000    0.217    0.000    1.126    0.000 random.py:334(randint)
#         1    0.000    0.000    1.330    1.330 task_1.py:22(min_2)
#         1    0.204    0.204    1.330    1.330 task_1.py:23(<listcomp>)
#         1    0.000    0.000    1.334    1.334 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   1000000    0.055    0.000    0.055    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1524878    0.093    0.000    0.093    0.000 {method 'getrandbits' of '_random.Random' objects}
# cProfile.run('min_1(10000000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.056    0.056   14.072   14.072 <string>:1(<module>)
#  10000000    3.318    0.000    4.660    0.000 random.py:237(_randbelow_with_getrandbits)
#  10000000    4.093    0.000    8.753    0.000 random.py:290(randrange)
#  10000000    2.182    0.000   10.935    0.000 random.py:334(randint)
#         1    0.611    0.611   14.015   14.015 task_1.py:12(min_1)
#         1    2.071    2.071   13.006   13.006 task_1.py:13(<listcomp>)
#         1    0.000    0.000   14.072   14.072 {built-in method builtins.exec}
#         2    0.074    0.037    0.074    0.037 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   4973298    0.323    0.000    0.323    0.000 {method 'append' of 'list' objects}
#  10000000    0.557    0.000    0.557    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  12736474    0.784    0.000    0.784    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# cProfile.run('min_2(10000000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.036    0.036   13.394   13.394 <string>:1(<module>)
#  10000000    3.575    0.000    5.064    0.000 random.py:237(_randbelow_with_getrandbits)
#  10000000    4.046    0.000    9.110    0.000 random.py:290(randrange)
#  10000000    2.188    0.000   11.298    0.000 random.py:334(randint)
#         1    0.000    0.000   13.358   13.358 task_1.py:22(min_2)
#         1    2.061    2.061   13.358   13.358 task_1.py:23(<listcomp>)
#         1    0.000    0.000   13.394   13.394 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#  10000000    0.556    0.000    0.556    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  15235645    0.933    0.000    0.933    0.000 {method 'getrandbits' of '_random.Random' objects}
# cProfile.run('min_1(100000000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.604    0.604  141.270  141.270 <string>:1(<module>)
# 100000000   33.215    0.000   46.712    0.000 random.py:237(_randbelow_with_getrandbits)
# 100000000   40.871    0.000   87.584    0.000 random.py:290(randrange)
# 100000000   21.850    0.000  109.434    0.000 random.py:334(randint)
#         1    6.117    6.117  140.666  140.666 task_1.py:12(min_1)
#         1   21.073   21.073  130.507  130.507 task_1.py:13(<listcomp>)
#         1    0.000    0.000  141.270  141.270 {built-in method builtins.exec}
#         2    0.729    0.364    0.729    0.364 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#  49751541    3.314    0.000    3.314    0.000 {method 'append' of 'list' objects}
# 100000000    5.614    0.000    5.614    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 127356842    7.884    0.000    7.884    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# cProfile.run('min_2(100000000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.406    0.406  134.008  134.008 <string>:1(<module>)
# 100000000   35.787    0.000   50.790    0.000 random.py:237(_randbelow_with_getrandbits)
# 100000000   40.391    0.000   91.181    0.000 random.py:290(randrange)
# 100000000   21.813    0.000  112.994    0.000 random.py:334(randint)
#         1    0.000    0.000  133.602  133.602 task_1.py:22(min_2)
#         1   20.608   20.608  133.602  133.602 task_1.py:23(<listcomp>)
#         1    0.000    0.000  134.008  134.008 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
# 100000000    5.635    0.000    5.635    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 152390784    9.369    0.000    9.369    0.000 {method 'getrandbits' of '_random.Random' objects}


# Сложность алгоритма линейная, так как с увеличением входных данных на порядок (10) скорость работы программы
# увеличивается на примерно такой же порядок (не обязательно сложность именно О(n), скорре всего она имеет сложность
# вида (k*n +b), но все равно от этого линейной она быть не перестает).
# При этом, исходя из анализа полученных данных, второй метод работает быстрее. Если я правильно понял данные,
# на list comprehension во втором случае тратится меньше времени, чем в первом. Если это так, то это достаточно странно,
# поскольку алгоритм создания списка идентичен в обоих случаях. Так же, второй способ работает быстрее, поскольку нет
# необходимости работать со списком отрицательных значений - второй способ только переопределяет две переменные, что
# по логике происходит быстрее. Так же по затратам памяти второй способ должен выигрывать, поскольку он не хранит
# отдельный список со всеми отрицательными элементами массива. Очень хотелось бы получить фидбэк по этим мыслям))

# Так же для понимая темы, взял алгоритм из задания № 1 ДЗ № 3: В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Выбрал это задание, поскольку здесь имеется двойной
# вложенный цикл for. Если я правильно понял полученные данные, то сложность работы у него так же линейная
# вида (k*n + m), поскольку при увеличении исходных данных в первои и втором массиве на 10 скорость
# выполнения возрастает в 100 с лишним раз. Если так, то это странно, поскольку функция имеет два вложенных цикла,
# а согласно методичке - это квадратичная сложность. Или я не прав?

def main(n, m):
    range_1 = [el for el in range(2, n)]
    range_2 = [el for el in range(2, m)]
    count = 0
    for el in range_1:
        for el_2 in range_2:
            if el % el_2 == 0:
                count += 1
    return (print(f'Количество кратных чисел: {count}'))


# cProfile.run('main(100, 10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:4(main)
#         1    0.000    0.000    0.000    0.000 task_2.py:5(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_2.py:6(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('main(1000, 100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.002    0.002    0.003    0.003 task_2.py:4(main)
#         1    0.000    0.000    0.000    0.000 task_2.py:5(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_2.py:6(<listcomp>)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('main(10000, 1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.265    0.265 <string>:1(<module>)
#         1    0.264    0.264    0.265    0.265 task_2.py:4(main)
#         1    0.000    0.000    0.000    0.000 task_2.py:5(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_2.py:6(<listcomp>)
#         1    0.000    0.000    0.265    0.265 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('main(100000, 10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001   31.912   31.912 <string>:1(<module>)
#         1   31.908   31.908   31.911   31.911 task_2.py:4(main)
#         1    0.003    0.003    0.003    0.003 task_2.py:5(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_2.py:6(<listcomp>)
#         1    0.000    0.000   31.912   31.912 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

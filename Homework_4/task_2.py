# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

# Анализ скорости работы алгоритма начинается с исходных данных от 50, поскольку для любых значений меньше 50
# скорость работы алгоритма равна 0.000.
#
# Мой мысли по поводу скорости и сложности данных методов написаны в самом низу под выходными данными cProfile

import cProfile


def simple_definition(m):
    num_list = [_ for _ in range(2, m * m)]
    simple_num = []

    for num in num_list:
        if all(num % i != 0 for i in range(2, num)):
            simple_num.append(num)
    return print(f'Простым числом под номером {m} является {simple_num[m-1]}')


def eratosthenes(m):
    num_list = [_ for _ in range(m * m)]
    simple_num = []
    i = 2

    while i < len(num_list):
        if num_list[i] != 0:
            simple_num.append(num_list[i])
            j = i * 2
            while j < len(num_list):
                num_list[j] = 0
                j = j + i
        i += 1
    return print(f'Простым числом под номером {m} является {simple_num[m-1]}')


# cProfile.run('simple_definition(50)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.070    0.070 <string>:1(<module>)
#         1    0.001    0.001    0.070    0.070 task_2.py:10(simple_definition)
#         1    0.000    0.000    0.000    0.000 task_2.py:11(<listcomp>)
#    429658    0.039    0.000    0.039    0.000 task_2.py:15(<genexpr>)
#      2498    0.029    0.000    0.068    0.000 {built-in method builtins.all}
#         1    0.000    0.000    0.070    0.070 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       367    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('eratosthenes(50)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.001    0.001    0.002    0.002 task_2.py:20(eratosthenes)
#         1    0.000    0.000    0.000    0.000 task_2.py:21(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      8143    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       367    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('simple_definition(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.958    0.958 <string>:1(<module>)
#         1    0.005    0.005    0.958    0.958 task_2.py:10(simple_definition)
#         1    0.000    0.000    0.000    0.000 task_2.py:11(<listcomp>)
#   5785220    0.557    0.000    0.557    0.000 task_2.py:15(<genexpr>)
#      9998    0.395    0.000    0.952    0.000 {built-in method builtins.all}
#         1    0.000    0.000    0.958    0.958 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('eratosthenes(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.005    0.005    0.007    0.007 task_2.py:20(eratosthenes)
#         1    0.000    0.000    0.000    0.000 task_2.py:21(<listcomp>)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#     34297    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('simple_definition(200)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   13.391   13.391 <string>:1(<module>)
#         1    0.024    0.024   13.390   13.390 task_2.py:10(simple_definition)
#         1    0.001    0.001    0.001    0.001 task_2.py:11(<listcomp>)
#  79448558    7.908    0.000    7.908    0.000 task_2.py:15(<genexpr>)
#     39998    5.457    0.000   13.363    0.000 {built-in method builtins.all}
#         1    0.000    0.000   13.391   13.391 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      4203    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('eratosthenes(200)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.031    0.031 <string>:1(<module>)
#         1    0.021    0.021    0.030    0.030 task_2.py:20(eratosthenes)
#         1    0.001    0.001    0.001    0.001 task_2.py:21(<listcomp>)
#         1    0.000    0.000    0.031    0.031 {built-in method builtins.exec}
#    143087    0.008    0.000    0.008    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      4203    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('eratosthenes(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.007    0.007    0.853    0.853 <string>:1(<module>)
#         1    0.594    0.594    0.846    0.846 task_2.py:20(eratosthenes)
#         1    0.030    0.030    0.030    0.030 task_2.py:21(<listcomp>)
#         1    0.000    0.000    0.853    0.853 {built-in method builtins.exec}
#   3853705    0.218    0.000    0.218    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#     78498    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('eratosthenes(10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.702    0.702   98.165   98.165 <string>:1(<module>)
#         1   70.109   70.109   97.463   97.463 task_2.py:20(eratosthenes)
#         1    3.337    3.337    3.337    3.337 task_2.py:21(<listcomp>)
#         1    0.000    0.000   98.165   98.165 {built-in method builtins.exec}
# 415037278   23.617    0.000   23.617    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   5761455    0.399    0.000    0.399    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Определение простого числа простым перебором работает в разы медленнее, чем через Решето. Проблема в использовании
# вложенных циклов - они очень сильно съедают ресурсы. По этой причине оценить скорость работы простого перебора
# при значениях больше 200 не представилось возможным - алгоритм просто считался очень долго, тогда как с помощью Решета
# было найдено простое число под номером 10 000.
# Сложность простого перебора - квадратичная, Решета - линейная. Буду рад услышать фидбэк))
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

seq = input('Введите последовательность чисел через пробел: ').split(' ')
number = input('Введите цифру, количество вхождений которой необходимо посчитать: ')
per = 0
for i in seq:
    per += i.count(number)
print(f'В введенной последовательности цифра {number} встречается {per} раз')

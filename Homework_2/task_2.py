# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Введите натурльное число: ')
even = []
uneven = []

for el in number:
    if int(el) % 2 == 0 or int(el) == 0:
        even.append(int(el))
    else:
        uneven.append((int(el)))

print(f'Количество четных цифр в числе {number} - {len(even)}, нечетных - {len(uneven)}')
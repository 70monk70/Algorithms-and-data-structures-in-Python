# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

seq = input('Введиие последовательность натуральных чисел через пробел: ').split(' ')
sum_seq = []
for i in seq:
    summ = 0
    for j in i:
        summ += int(j)
    sum_seq.append(summ)
print(f'Из введенной последовательности чисел наибольшим по сумме цифр является {seq[sum_seq.index(max(sum_seq))]}.\n'
      f'Сумма его элементов равна {max(sum_seq)}')
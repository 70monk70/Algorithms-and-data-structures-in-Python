a = str(input('Введите трехзначное число: '))
summ = 0
comp = 1

if len(a) == 3:
    for el in a:
        summ += int(el)
        comp *= int(el)
    print(f'Сумма цифр числа {a}: {summ}')
    print(f'Произведение цифр числа {a}: {comp}')
else:
    print('Число не трехзначное')
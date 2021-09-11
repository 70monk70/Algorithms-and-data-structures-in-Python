matrix = [[] for el in range(4)]

for line in matrix:
    summ = 0
    for num in range(4):
        num = int(input('Введите значение: '))
        line.append(num)
        summ += num
    line.append(summ)

for line in matrix:
    for num in line:
        print(f'{num:5}', end='')
    print()
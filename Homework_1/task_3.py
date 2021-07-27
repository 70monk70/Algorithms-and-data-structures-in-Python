x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))

if x1 != x2:
    k = (y2 - y1) / (x2 - x1)
    b = (x2*y1 - x1*y2)/(x2 - x1)
    print(f'Уравнение прямой: y = {k} * x + {b}')
else:
    print(f'Уравнение прямой: y = 0')
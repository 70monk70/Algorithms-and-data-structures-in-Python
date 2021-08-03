# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

range_1 = [el for el in range(2, 100)]
range_2 = [el for el in range(2, 10)]
count = 0

for el in range_1:
    for el_2 in range_2:
        if el % el_2 == 0:
            count += 1

print(f'Количество кратных чисел: {count}')

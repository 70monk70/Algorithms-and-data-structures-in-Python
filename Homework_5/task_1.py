# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль
# ниже среднего.

import collections
while True:
    try:
        num_of_company = int(input('Введите количество компаний: '))
    except ValueError:
        print('Вы ввели недопустимое значение!')
        continue
    break

companies = collections.defaultdict()
profit_above_average = collections.deque()
profit_below_average = collections.deque()
profit_of_all_companies = 0
quater = 4


for el in range(num_of_company):
    name = input(f'\nВведите название {el+1}й компании: ')
    profit = 0
    q = 1
    while q <= quater:
        try:
            profit += float(input(f'Введите прибыль за {q}й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение!')
            continue
        q += 1
    companies[name] = profit
    profit_of_all_companies += profit

average_profit = profit_of_all_companies / num_of_company

for i, item in companies.items():
    if item >= average_profit:
        profit_above_average.append(i)
    else:
        profit_below_average.append(i)

print(f'\nСредняя прибыль для всех компаний: {average_profit}\n'
      f'Прибыль выше среднего у {len(profit_above_average)} компаний: {", ".join(profit_above_average)}\n'
      f'Прибыль ниже среднего у {len(profit_below_average)} компаний: {", ".join(profit_below_average)}')

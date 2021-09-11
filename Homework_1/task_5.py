import string

print('Введите две прописные буквы латинского алфавита')
let1 = input('Первая буква: ').lower()
let2 = input('Вторая буква: ').lower()
pos1 = (string.ascii_lowercase).index(let1) + 1
pos2 = (string.ascii_lowercase).index(let2) + 1
distance = abs(pos1 - pos2) - 1
print(f'Буква {let1} - {pos1}-я буква в алфавите\n'
      f'Буква {let2} - {pos2}-я буква в алфавите\n'
      f'Между буквами {let1} и {let2} находится ещё {distance}')

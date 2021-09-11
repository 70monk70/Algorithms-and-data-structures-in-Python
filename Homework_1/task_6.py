import string

let = int(input('Введите номер буквы латинского алфавита, которую хотите определить: '))
if let <= 26:
    print(f'Буква с номером {let} - {string.ascii_lowercase[let - 1]}')
else:
    print('Буквы с таким номером в латинском алфавите нет!')
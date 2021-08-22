# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
# только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib


def substr(s):
    str_lst = []

    for el in range(1, len(s)):
        for i in range(len(s) - el + 1):
            h_sub = hashlib.sha1(s[i:i + el].encode('utf-8')).hexdigest()
            if h_sub not in str_lst:
                str_lst.append(s[i:i + el])

    if len(str_lst) > 0:
        return f'В строке "{s}" найдено {len(str_lst)} уникальных подстрок: \n{str_lst}'
    return 'Пустая строка'


s = input('Введите строку: ')
print(substr(s))

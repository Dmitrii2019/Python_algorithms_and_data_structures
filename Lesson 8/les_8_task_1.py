# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
import hashlib

line = 'sova'
hash_ = []


def number_substrings(line):
    count = 0
    len_line = len(line)
    for i in range(len_line):
        for j in range(len_line + 1):
            if line[i:j] != line and line[i:j] != '':
                if hashlib.sha256(line[i:j].encode('utf-8')).hexdigest() not in hash_:
                    hash_.append(hashlib.sha256(line[i:j].encode('utf-8')).hexdigest())
                    count += 1
    return count


print(f'Количество различных подстрок в строке "{line}" = {number_substrings(line)}')

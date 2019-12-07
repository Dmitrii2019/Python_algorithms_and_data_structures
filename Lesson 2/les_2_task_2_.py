# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1DAcu7oDHII99pHzDmNOmWK8jNV9WTsw5/view?usp=sharing

number = input('Введите натурального число: ')
even = 0
not_even = 0
for i in number:
    if int(i) % 2 == 0:
        even = even + 1
    else:
        not_even = not_even + 1

print(f'четные = {even}, нечетные = {not_even}')

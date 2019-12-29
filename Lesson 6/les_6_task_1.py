# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
from sys import getsizeof


def sum_variables(*args):
    variables = (args)
    sum_ = 0
    for i in variables:
        sum_ += getsizeof(type(i)) + getsizeof(i)
    return sum_

# *************************1*Вариант********************************

spam_i = None  # для учета памяти

value = 1
max_namber = 0
spam = 0
max_sum = 0
while value != 0:
    value = int(input('введите натуральные числа: '))
    if value != 0:
        spam = 0
        for i in str(value):
            spam += int(i)
            spam_i = i  # для учета памяти
        if spam > max_sum:
            max_sum = spam
            max_namber = value

print(f'число {max_namber}, сумма его цифр {max_sum}')
print(f'Выриант 1 = {sum_variables(spam_i, value, max_namber, spam, max_sum)}')
# введите натуральные числа: 234
# введите натуральные числа: 567
# введите натуральные числа: 0
# число 567, сумма его цифр 18
# Выриант 1 = 2238
# # *************************2*Вариант********************************

spam_i = None  # для учета памяти
spam = None  # для учета памяти

value = 1
dict_ = {}
while value != 0:
    value = input('введите натуральные числа: ')
    if value != '0':
        spam = 0
        for i in value:
            spam += int(i)
            spam_i = i  # для учета памяти
        dict_[spam] = value
    else:
        break

print(f'число {dict_[max(dict_)]}, сумма его цифр {max(dict_.keys())}')
print(f'Выриант 2 = {sum_variables(spam_i, spam, value, dict_)}')
# введите натуральные числа: 234
# введите натуральные числа: 567
# введите натуральные числа: 0
# число 567, сумма его цифр 18
# Выриант 2 = 2024
# *************************3*Вариант********************************

spam_i = None  # для учета памяти
spam_sum_ = None  # для учета памяти

value = 1
max_nam = ()
max_sum = 0
while value != 0:
    value = tuple(input('введите натуральные числа: '))
    if value != tuple('0'):
        sum_ = sum([i for i in range(int(value[0]), int(value[-1]) + 1)])
        spam_i = int(value[-1]) + 1  # для учета памяти
        spam_sum_ = sum_  # для учета памяти
        if sum_ > max_sum:
            max_sum, max_nam = sum_, value
    else:
        break

spam_i_1 = None  # для учета памяти
max_namber = ''
for i in max_nam:
    max_namber += i
    spam_i = i

print(f'число {max_namber}, сумма его цифр {max_sum}')
print(f'Выриант 3 = {sum_variables(spam_i, spam_sum_, value, max_nam, max_sum, spam_i_1, max_namber)}')

# введите натуральные числа: 234
# введите натуральные числа: 567
# введите натуральные числа: 0
# число 567, сумма его цифр 18
# Выриант 3 = 3198

# Вариант под номером 2, меньше всего заняль памяти, так как для определения максимальнальной суммы чисел
# использовал функцию, а не допольнительную переменую, хотя сам тип данных dict занимает больше места, на очень большом
# количестве данных, на первое месты выйдет вариант 1, так как он постояно обнуляет переменные max_namber и max_sum
# а вариант 2 постояно расширяет переменую dict_
# Вывод если много чисел будет сравниваться вариан 1
# если не большое количество вариант 2

# разнообразие задач сделал по исползовании типа данных, у всех принцеп один, в основном чем больше переменных тем
# больше памяти занимает программа
# разрядность ОС 64 и интерпретатора Python 3.8;
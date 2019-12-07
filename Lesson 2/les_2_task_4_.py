# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
# 1, -0.5, 0.25, -0.125
# https://drive.google.com/file/d/1XfO3PrEPI4BdTMBvYkTgfmHrhxetqHmH/view?usp=sharing

n = input('Количество элементов: ')
n = int(n)
a = 1
c = 0
while n > 0:
    c += a
    a = a / -2
    n = n - 1

print(c)

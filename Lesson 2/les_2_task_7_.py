# Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n — любое натуральное число.
# https://drive.google.com/file/d/11WnhUFUKmHN2OISeizL40FicvxEo4vbf/view?usp=sharing

n = input('Введите натуральное число: ')
n1 = int(n)
a = 1
sum1 = 0
while n1 > 0:
    sum1 += a
    a += 1
    n1 -= 1


n = int(n)
sum2 = n * (n + 1) / 2

if sum1 == sum2:
    print('Значения совпадают')
else:
    print('Значения не совпадают')

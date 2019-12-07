# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
# https://drive.google.com/file/d/1-BSYCz6FPaYhwOz8oHjtRgO8dLHpwBTF/view?usp=sharing

a = 1
b = 0
c = 0
e = 0
while a != 0:
    a = int(input('введите натуральные числа: '))
    if a != 0:
        c = 0
        for i in str(a):
            c = c + int(i)
            if a > b:
                b = a
            if c > e:
                e = c

print(f' число {b}, сумма его цифр {e}')

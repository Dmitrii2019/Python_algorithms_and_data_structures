# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://drive.google.com/file/d/1sPAwzRiRs0xYN699s8KpcZPNsYm2G7qt/view?usp=sharing

a = int(input(' Введите 1 число: '))
b = int(input(' Введите 2 число: '))
c = int(input(' Введите 3 число: '))

if c > a > b or b > a > c:
    print(f'среднее чесло {a}')
elif a > c > b or b > c > a:
    print(f'среднее чесло {c}')
else:
    print(f'среднее чесло {b}')

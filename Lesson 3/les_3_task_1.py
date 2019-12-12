# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

from_before = [i for i in range(2, 9 + 1)]
number = [i for i in range(2, 99 + 1)]

# print(number)
# print(from_before)
nub = 0

for i in from_before:
    nub = 0
    for itm in number:
        if itm == 99:
            if itm % i == 0:
                nub += 1
            print(f'{i} кратно {nub} раз в диапазоне от 2 до 99')
        elif itm % i == 0:
            nub += 1

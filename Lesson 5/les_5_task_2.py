# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import Counter, deque

numbers = Counter(
    '122333444455555666666777777788888888999999999AAAAAAAAAABBBBBBBBBBBCCCCCCCCCCCCDDDDDDDDDDDDDEEEEEEEEEEEEEEFFFFFFFFFFFFFFF')
numbers['0'] = 0

f = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

number_1 = deque(input('Введите 1-е число:').upper())
number_2 = deque(input('Введите 2-е число:').upper())

if len(number_1) < len(number_2):
    while len(number_1) < len(number_2):
        number_1.appendleft(0)
else:
    while len(number_2) < len(number_1):
        number_2.appendleft(0)

number_1.reverse()
number_2.reverse()

number_1 = Counter(number_1)
number_2 = Counter(number_2)

result = []
balance = 0
for i in number_1.copy():
    if number_1[i] == 1:
        number_1[i] = numbers[i]
        for itm in number_2:
            number_2[itm] = numbers[itm]
            sum_ = number_1[i] + number_2[itm] + balance
            number_2.pop(itm)
            balance = 0
            if sum_ > 15:
                sum_ = sum_ - 16
                if sum_ > 9:
                    result.append(f[sum_])
                elif sum_ < 9:
                    result.append(sum_)
                balance = balance + sum_
            elif 9 < sum_ < 15:
                result.append(f[sum_])
            elif sum_ == 15:
                result.append('F')
            else:
                result.append(sum_)
            break
    else:
        print('Одинаковые значения не работает')

result.reverse()

print(result)

# Програма работает плохо, не хватило времени разобраца, выкладываю, что бы видели, что пытался, не судите строго


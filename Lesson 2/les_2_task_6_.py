# . В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше
# введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.
# https://drive.google.com/file/d/1S1fqZ9EKPKZ9CqUdkerlKPVu7jJYXhEx/view?usp=sharing

import random

n = random.randint(0, 100)
attempts = 10
while attempts > 0:
    value = int(input('введите чесло от 0 до 100: '))
    if value == n:
        print('вы угадали')
        break
    elif value > n:
        print('число меньше вашего ответа')
    else:
        print('число больше вашего ответа')
    attempts -= 1
print(f'Вы проиграли, правильный ответ {n}')

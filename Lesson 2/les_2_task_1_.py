# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак
# (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
# https://drive.google.com/file/d/1a0aqLtz5IA8auG_bpdfTWp5qe6E21eR9/view?usp=sharing

def check():
    sign1 = str(input('знак '))
    if sign1 == '0':
        return sign1
    elif sign1 != '+' and sign1 != '-' and sign1 != '*' and sign1 != '/':
        print('ошибка, 0 - выход, +, -, *, /')
        sign1 = check()
    return sign1


def inputs():
    a = int(input('1-е число: '))
    sign = check()
    if sign == '0':
        print('end')
    else:
        b = int(input('2-е число: '))
        if sign == '/' and b == 0:
            print('не дели на ноль')
            inputs()
        else:
            results(a, sign, b)


def results(a, sign, b):
    if sign == '+':
        print(a + b)
    elif sign == '-':
        print(a - b)
    elif sign == '*':
        print(a * b)
    else:
        print(a / b)
    inputs()


inputs()

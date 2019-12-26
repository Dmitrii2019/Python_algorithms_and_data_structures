# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1sPAwzRiRs0xYN699s8KpcZPNsYm2G7qt/view?usp=sharing

namber = int(input('введите чесло: '))
a = namber // 100
b = (namber // 10) % 10
c = namber % 10
print(f'сумма цифр = {a + b + c}, произведение цифр = {a * b * c}')

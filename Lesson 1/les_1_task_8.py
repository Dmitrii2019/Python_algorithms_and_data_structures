# Определить, является ли год, который ввел пользователь, високосным или не високосным.
# высокостный 1600 2000 2016 2020
# не высокостный 1700 1800 1900 2017
# https://drive.google.com/file/d/1sPAwzRiRs0xYN699s8KpcZPNsYm2G7qt/view?usp=sharing

year = int(input('введите год: '))
if year % 100 == 0:
    if year % 400 == 0:
        print(f'{year} год высокостный')
    else:
        print(f'{year} год не высокостный')
else:
    if year % 4 == 0:
        print(f'{year} год высокостный')
    else:
        print(f'{year} год не высокостный')

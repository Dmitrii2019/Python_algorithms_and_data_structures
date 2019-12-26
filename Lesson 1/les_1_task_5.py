# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# https://drive.google.com/file/d/1sPAwzRiRs0xYN699s8KpcZPNsYm2G7qt/view?usp=sharing

letter_1 = input('Ввидите первую букву: ')
letter_2 = input('Ввидите вторую букву: ')
place_letters_1 = ord(letter_1)
place_letters_2 = ord(letter_2)
between_letters = place_letters_1 - place_letters_2
if between_letters < 0:
    between_letters = between_letters * -1

print(f'{place_letters_1}, {place_letters_2}, между ними {between_letters}')

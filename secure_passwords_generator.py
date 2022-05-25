import random
digit, symbols = '0123456789', '~`!@#$%^&*()-+='
letters_lower, letters_upper = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
temp = ''
print('Добро пожаловать на борт генерации рандомных паролей!')
print()

pass_count = input('Сколько нужно сгенерировать паролей? Введите число: ')
if not pass_count.isdigit():
    pass_count = input('Сколько нужно сгенерировать паролей? Введите именно число от "1" до бесконечности: ')
else:
    pass_count = int(pass_count)

pass_len = input('Какая должна быть длина одного пароля? Введите число: ')
if not pass_len.isdigit():
    pass_len = input('Какая должна быть длина одного пароля? Введите именно число от "1" до бесконечности: ')
else:
    pass_len = int(pass_len)

digit_include = input(f'Нужно ли включать в пароль цифры "{digit}"? Введите "да" или "нет": ')
while True:
    if digit_include != 'да' and digit_include != 'нет':
        digit_include = input(f'Нужно ли включать в пароль цифры "{digit}"? Введите либо "да", либо "нет": ')
    elif digit_include == 'да':
        temp += digit
        break
    else:
        break

letters_upper_include = input(f'Нужно ли включать в пароль большие буквы "{letters_upper}"? Введите "да" или "нет": ')
while True:
    if letters_upper_include != 'да' and letters_upper_include != 'нет':
        letters_upper_include = input(f'Нужно ли включать в пароль большие буквы "{letters_upper}"? Введите либо ' +\
                                      '"да", либо "нет": ')
    elif letters_upper_include == 'да':
        temp += letters_upper
        break
    else:
        break

letters_lower_include = input(f'Нужно ли включать в пароль маленькие буквы "{letters_lower}"? Введите "да" или "нет": ')
while True:
    if letters_lower_include != 'да' and letters_lower_include != 'нет':
        letters_lower_include = input(f'Нужно ли включать в пароль маленькие буквы "{letters_lower}"? Введите либо ' +\
                                      '"да", либо "нет": ')
    elif letters_lower_include == 'да':
        temp += letters_lower
        break
    else:
        break

symbols_include = input(f'Нужно ли включать в пароль символы по типу "{symbols}"? Введите "да" или "нет": ')
while True:
    if symbols_include != 'да' and symbols_include != 'нет':
        symbols_include = input(f'Нужно ли включать в пароль символы "{symbols}"? Введите либо "да", либо "нет": ')
    elif symbols_include == 'да':
        temp += symbols
        break
    else:
        break

pohozhue_symbols = input('Нужно ли ИСКЛЮЧАТЬ неоднозначные символы по типу "il1Lo0O"? Введите "да" или "нет": ')
while True:
    if pohozhue_symbols != 'нет' and pohozhue_symbols != 'да':
        pohozhue_symbols = input('Нужно ли ИСКЛЮЧИТЬ из паролей похожие внешне символы "il1Lo0O"? Введите "да" если ' +\
                                 'нужно ИСКЛЮЧИТЬ, либо "нет" - если исключить НЕ нужно: ')
    elif pohozhue_symbols == 'да':
        temp = ''.join([i for i in temp if i not in 'il1Lo0O'])
        break
    else:
        break

def generate_password(lenght, chars):
    password = ''
    for i in range(pass_len):
        password += random.choice(temp)
    return password

for _ in range(pass_count):
    print(generate_password(pass_len, temp))

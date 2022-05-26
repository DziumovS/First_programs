def caesar_cipher(direction, rot_n, user_text):
    for i in range(len(user_text)):
        if user_text[i].isalpha() and direction == 'зашифровать':
            if user_text[i].islower():
                print(low_lett[(low_lett.index(user_text[i]) + rot_n) % len_lett], end='')
            elif user_text[i].isupper():
                print(upp_lett[(upp_lett.index(user_text[i]) + rot_n) % len_lett], end='')
        elif user_text[i].isalpha() and direction == 'расшифровать':
            if user_text[i].islower():
                print(low_lett[(low_lett.index(user_text[i]) - rot_n) % len_lett], end='')
            elif user_text[i].isupper():
                print(upp_lett[(upp_lett.index(user_text[i]) - rot_n) % len_lett], end='')
        else:
            print(user_text[i], end='')


direction = input('Нужно зашифровать или расшифровать? Уточните:\n').lower()
while direction != 'зашифровать' and direction != 'расшифровать':
    direction = input('Нужно выбрать и написать: либо "зашифровать", либо "расшифровать. Повторите ввод:\n').lower()

language = input('На каком языке будем страдать: "английском" или "русском"? Уточните:\n').lower()
while language != 'английский' and language != 'русский':
    language = input('Нужно выбрать и написать: либо "английский", либо "русский". Повторите ввод:\n').lower()
if language == 'английский':
    low_lett, upp_lett, len_lett = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26
else:
    low_lett, upp_lett, len_lett = 'абвгдежзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 32

rot_n = input('Какой должен быть сдвиг? Укажите число:\n')
while not rot_n.isdigit():
    rot_n = input('Нужно указать размер сдвига: число от "1" до бесконечности. Повторите ввод:\n')
rot_n = int(rot_n)

user_text = input(f'Введите текст, который нужно {direction}, на языке {language}:\n')
while user_text.isdigit() or user_text.isspace():
    user_text = input('"Шифр Цезаря" предполагает работу с буквами. Введите корректный текст, чтобы он содержал'+\
                      f'буквы на выбранном вами {language} языке, который нужно {direction}:\n')

caesar_cipher(direction, rot_n, user_text)
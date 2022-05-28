from random import *
words = ['АРБУЗ', 'АНАНАС', 'АВТОМОБИЛЬ', 'КАКАШКА', 'ПОКЕМОН', 'ТЕЛЕВИЗОР', 'СОБАКА', 'ЧЕЛОВЕК', 'РОБОТ', 'КОМПЬЮТЕР',
         'ДОМ', 'ЧИПОЛИНО', 'НЕБО', 'ПОБЕДА', 'ДРУЖБА', 'МИР', 'АЙФОН', 'ЛИСТ', 'ДОМКРАТ', 'ТРУПЕРДА', 'ТРАНКВИЛИЗАТОР']

gallows_6 = '▄▄▄▄▄▄▄\n' \
    ' ( )  █\n' \
    '      █\n' \
    '      █'
gallows_5 = gallows_6.replace(' ( )  █', ' (o)  █')
gallows_4 = gallows_5.replace('      █', '  |   █', 1)
gallows_3 = gallows_4.replace('  |   █', ' /|   █')
gallows_2 = gallows_3.replace(' /|   █', ' /|\\  █')
gallows_1 = gallows_2.replace('      █', ' /    █')
gallows_0 = gallows_1.replace(' /    █', ' / \\  █')

def get_word():
    return choice(words)

def display_hangman(tries):
    stages = [gallows_0, gallows_1, gallows_2, gallows_3, gallows_4, gallows_5, gallows_6]
    return stages[tries]

def play(word):
    word_len, named_letters, named_words, tries = '_' * len(word), [], [], 6
    print(f'Добро пожаловать в игру "Виселица".\n'
          f'{display_hangman(tries)}\n'
          f''
          'Правила достаточно просты:\n'
          '1) Я, программа, загадываю тебе слово.\n'
          '2) Ты, человек, должен его отгадать называя буквы, при этом у тебя есть только 6 попыток:\n'
          ' 2.1) в случае, если отгадал букву - я тебе выведу на экран её столько раз, сколько она содержится в слове\n'
          ' 2.2) если указал букву, которой в слове нет - на виселице начнет формироваться "человечек"\n'
          ' 2.3) всего человечек состоит из 6 конечностей:\n'
          '   - голова\n'
          '   - туловище\n'
          '   - левая рука\n'
          '   - правая рука\n'
          '   - левая нога\n'
          '   - правая нога\n'
          '3) В случае, если на виселице появится "человечек" состоящий из всех 6-ти конечностей - ты ПРОИГРАЛ.\n'
          '4) Чтобы выйти из игры, досрочно прервав её - введи слово "выйти".\n'
          f'Да начнется же игра!\n'
          f''
          f'Длина загаданного слова состоит из {len(word)} букв:\n'
          f'{word_len}\n'
          f'\n')

    while True:
        user_text = input('Введите букву или, если знаете, слово целиком:\n').upper()
        while not user_text.isalpha():
            user_text = input('Нужно ввести или БУКВУ или, если знаете, СЛОВО целиком. Повторите ввод:\n').upper()
        if user_text == 'выйти' or user_text == 'ВЫЙТИ':
            return print('Что ж, сыграем как-нибудь в другой раз. Прощай.')

        if len(user_text) != 1:
            if user_text == word:
                return print('Поздравляю, вы угадали слово и победили!')
            else:
                if user_text in named_words:
                    print('Вы уже называли это слово, это неправильный ответ.')
                else:
                    named_words.append(user_text)
                    tries -= 1
                    if tries == 0:
                        return print(f'К сожалению, у вас осталось {tries} попыток.\n'
                                     f'Вы проиграли :(\n'
                                     f'Загаданным словом было слово "{word}".')
                    else:
                        print('Это не то слово, что было загадано, попробуйте еще раз.\n'
                          f'У вас осталось {tries} попыток.\n'
                          f'{display_hangman(tries)}\n'
                          f'{word_len}')

        elif len(user_text) == 1:
            if user_text in word:
                if user_text in named_letters:
                    print('Вы уже называли эту букву, попробуйте другу.')
                else:
                    named_letters.append(user_text)
                    for i in range(len(word)):
                        if word[i] == user_text:
                            word_len = word_len[:i] + user_text + word_len[i + 1:]
                    print('Вы угадали букву!\n'
                          f'В загаданном слове количество этой буквы равно {word.count(user_text)}.\n'
                          f'{word_len}')
                    if word_len.count('_') == 0:
                        return print(f'Поздравляю, вы угадали слово и победили!\n'
                              f'Загаданным словом было слово "{word}".')
                    else:
                        print(f'У вас осталось {tries} попыток и {word_len.count("_")} неотгаданных букв.\n'
                              f'Также напомню, что процесс отгадаывания слова следующий: {word_len}.\n'
                              f'А состояние вашей виселицы:\n'
                              f'{display_hangman(tries)}')
            elif user_text not in word:
                named_letters.append(user_text)
                tries -= 1
                if tries == 0:
                    return print(f'К сожалению, у вас осталось {tries} попыток.\n'
                                 f'Вы проиграли :(\n'
                                 f'Загаданным словом было слово "{word}".')
                else:
                    print('Этой буквы нет в слове, попробуйте еще раз.\n'
                          f'У вас осталось {tries} попыток и {word_len.count("_")} неотгаданных букв.\n'
                          f'Также напомню, что процесс отгадаывания слова следующий: {word_len}.\n'
                          f'А состояние вашей виселицы:\n'
                          f'{display_hangman(tries)}\n'
                          f'')

play(get_word())
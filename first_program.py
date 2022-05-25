from random import randint

num = randint(11, 100100)
while True:
    n = input('Сыграем в игру по угадыванию чисел? Введи число от 11 до 100100 [или нажми "q" для выхода]: ')
    if n == 'q':
        print(' - Эх ты, слабак. Ладно, поиграли и будет.')
        break
    elif not n.isdigit() or (11 > int(n) or int(n) > 100100):
        print(' - Так не пойдёт. Либо угадываешь, вводя число от 11 до 100100, либо пишешь букву "q", чтобы ' + \
              'закончить. Понял, да?')
    elif int(n) > num:
        print(' - Слишком много, попробуй еще раз.')
    elif int(n) < num:
        print(' - Слишком мало, попробуй еще раз.')
    else:
        print(' - Воу, угадал, красава, поздравляю!')
        break

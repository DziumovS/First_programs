user_text = input()

low_lett, upp_lett, len_lett = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26

def caesar_cipher(user_text):
    user_text_lst = user_text.split()
    for i in range(len(user_text_lst)):
        len_letter = 0
        for j in user_text_lst[i]:
            if j.isalpha():
                len_letter += 1
        for l in user_text_lst[i]:
            if l.islower():
                print(low_lett[(low_lett.index(l) + len_letter) % len_lett], end='')
            elif l.isupper():
                print(upp_lett[(upp_lett.index(l) + len_letter) % len_lett], end='')
            else:
                print(l, end='')
        if len_letter != 0:
            print(end=' ')

caesar_cipher(user_text)
number = input('Укажите число, которое необходимо перевести в другую систему счисления:\n')
while not number.isdigit():
    number = input('Укажите ЧИСЛО (а не текст / знаки), которое нужно перевести в другую систему счисления:\n')
number_true = int(number)

notation = input('Укажите в какую систему счисления нужно перевести число. Введите ответ числом:\n')
while not notation.isdigit():
    notation = input('Введите ЧИСЛО - в какую систему счисления нужно перевести введенное вами ранее число:\n')
notation = int(notation)

answer, values = '', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while number_true != 0:
    temp = number_true % notation
    answer = str(values[temp]) + answer
    number_true //= notation
print(f'{number} в {notation}-ной системе счисления это:\n{answer}')



# def number_systems_converter(your_number, notation):
#     answer, your_number_static, values, = '', your_number, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F',
#                                                             'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
#                                                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     while your_number != 0:
#         temp = your_number % notation
#         answer = str(values[temp]) + answer
#         your_number //= notation
#     print(f'{your_number_static} в {notation}-ной системе счисления это:\n{answer}')
#
# number_systems_converter(your_number, notation)
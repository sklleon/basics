"""
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""
my_list = []
while True:
    my_input = input('Введите все что угодно или окончании ввода данных будет свидетельствовать пустая строка " " : ')
    # my_list.append(my_input) if my_input != 'q' else: break
    if my_input != ' ':
        my_list.append(my_input + '\n')
    else:
        break
try:
    with open('task_5_1.txt', 'w', encoding='utf-8') as out_list:
        out_list.writelines(my_list)
except ValueError as err:
    print(err)

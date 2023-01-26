"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

translater = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
my_result = []
try:
    with open('task_5_4.txt', 'r+', encoding='utf-8') as file_obj:
        for line in file_obj:
            tokens = line.split(' - ')
            if tokens[0] in translater:
                word = translater[tokens[0]]
                my_result.append(f'{word} - {tokens[1]}')
except ValueError as err:
    print(f'Произошла ошибка {err}')

try:
    with open('task_5_4_out.txt', 'w+', encoding='utf-8') as file_input:
        file_input.writelines(my_result)
except ValueError as err2:
    print(f'Произошла ошибка {err2}')

"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""
my_temp = ['Привет\n', 'Как твои дела\n', 'Пока\n']

total_characters = 0
total_lines = 0

with open('task_5_2.txt', 'r+', encoding='utf-8') as in_file:
    in_file.writelines(my_temp)
    for f_line in in_file:
        total_characters += len(f_line) - 1
        total_lines += f_line.count('\n')
    print(total_characters, total_lines)
    in_file.writelines(f'Всего обработано {total_characters} букв в {total_lines} строк')

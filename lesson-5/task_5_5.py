"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""


def summary():
    try:
        with open('task_5_5.txt', 'w+') as file_obj:
            while True:
                character_input = input('Введите цифры через пробел, окончании выхода из программы будет свидетельствовать "q": ')
                if character_input == 'q':
                    break
                else:
                    file_obj.writelines(character_input)
                    my_numb = character_input.split()
                    print(sum(map(int, my_numb)))
    except ValueError as err:
        print(err)


summary()

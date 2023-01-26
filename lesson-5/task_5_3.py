"""
3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

firm = {'Иванов': 170000, 'Петров': 210000, 'Сидоров': 190000, 'Галкин': 150000, 'ЗАЙКА': 350000, 'Палкин': 550000, 'Балкин': 100000, 'Салкин': 150000, 'Какин': 250000, 'Макин': 350000, 'Фалкин': 150000, 'Заликин': 125000}
try:
    with open("task_5_3.txt", 'w+', encoding='utf-8') as file_obj:
        for last_name, salary in firm.items():
            file_obj.write(f'{last_name}  : {salary} \n')

except ValueError as err:
    print(f"Произошла ошибка {err}")

my_average = 0
my_count = 0
employees = []
tokens = 0
my_result = 0

try:
    with open("task_5_3.txt", 'r', encoding='utf-8') as in_file:
        for f_line in in_file:
            # print(f_line, end="")
            tokens = f_line.split(':')
            if int(tokens[1]) <= 200000:
                employees.append(tokens[0])
            my_average += int(tokens[1])
            my_count += 1
    # my_result =  my_average / my_count
    my_result = float(my_average / my_count)

    print(f"Сотрудники {employees} имеет оклад менее 200 тысяч")
    print(f"Подсчёт средней величины дохода сотрудников: {my_result}")

except ValueError as err:
    print(f"Произошла ошибка {err}")


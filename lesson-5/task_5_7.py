"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json


def get_stat():
    try:
        with open('task_5_7.txt', 'r+', encoding='utf-8') as my_file_in:
            stat = []
            profit = {}
            average_profit = {}
            bla = 0
            prof = 0
            i = 3
            for line in my_file_in:
                name, firm, earning, damage = line.split()
                total = int(earning) - int(damage)
                if total >= 0:
                    prof = prof + total
                else:
                    i -= 1
                profit[name] = total
            stat.append(profit)
            if i != 0:
                (bla) = prof / i
                average_profit['average_profit'] = round(bla)
                stat.append(average_profit)
            else:
                print('Все компании работают в убыток')
            print(stat)
        with open('task_5_7.json', 'a+', encoding='utf-8') as json_file:
            json.dump(stat, json_file)
    except ValueError as err:
        print(f'Произошла ошибка {err}')


get_stat()

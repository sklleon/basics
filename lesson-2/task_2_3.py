# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

# Вариант решения 1
list_seasons = ['Зима', 'Весна', 'Лето', 'Осень']
dict_months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь',
               11: 'Ноябрь',
               12: 'Декабрь'}

while True:
    cho = int(input('Введите месяц в виде целого числа от 1 до 12: '))
    if cho > 0 and cho < 13:
        if cho == 12 and cho <= 2:
            print(f'Это месяц: {dict_months.get(cho)} время года: {list_seasons[0]}')
            break
        elif cho >= 3 and cho <= 5:
            print(f'Это месяц: {dict_months.get(cho)} время года: {list_seasons[1]}')
            break
        elif cho >= 6 and cho <= 8:
            print(f'Это месяц: {dict_months.get(cho)} время года: {list_seasons[2]}')
            break
        else:
            print(f'Это месяц: {dict_months.get(cho)} время года: {list_seasons[3]}')
            break
    else:
        print('Неверно указано число')

# Вариант решения 2

dict_months = {'Зима': [12,1,2], 'Весна': [3,4,5], 'Лето': [6,7,8], 'Осень': [9,10,11]}
cho = int(input('Введите месяц в виде целого числа от 1 до 12: '))

if cho in sum(dict_months.values(),[]):
    for i in dict_months.items():
        if cho in i[1]:
            print(i[0])
            break

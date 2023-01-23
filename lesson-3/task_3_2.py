# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
# version 1
def user_data(first_name, last_name, year_birth, city_residence):
    return print(
        f'Получается Ваше Имя: {first_name} Фамилия: {last_name} Год рождения: {year_birth} Город проживания: {city_residence}')


user_data(first_name=input('Введите Ваше Имя: '),
          last_name=input('А теперь Фамилию: '),
          year_birth=input('Год рождения: '),
          city_residence=input('Город проживания: ')
          )

# version 2
my_line = input('Введите свое - имя, фамилия, год рождения, город одной строкой: ').split()


def my_function(first_name, last_name, year_birth, city_residence):
    return (f'Получается Ваше Имя: {first_name}, Фамилия: {last_name}, Год рождения: {year_birth}, Город проживания: {city_residence}')


print(my_function(my_line[0], my_line[1], my_line[2], my_line[3]))

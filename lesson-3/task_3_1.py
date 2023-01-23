# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_function(argument1, argument2):
    try:
        a = int(argument1)
    except ValueError as err:
        return (f'Причина Ошибки в аргументе 1 - {err}')
    try:
        b = int(argument2)
    except ValueError as err:
        return (f'Причина Ошибки в аргументе 2 - {err}')
    division = a / b if b > 0 else ('На ноль делить нельзя ')
    return division
print(my_function(input('Введите числовой Аргумент 1: '), input('Введите числовой Аргумент 2: ')))

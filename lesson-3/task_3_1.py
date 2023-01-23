# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_function(argument1, argument2):
    try:
        a = int(argument1)
        b = int(argument2)
    except ValueError as err:
        return (f'Причина Ошибки : {err}')
    division = a / b if b > 0 else ('На ноль делить нельзя ')
    return division
print(my_function(input('Введите числовой Аргумент 1: '), input('Введите числовой Аргумент 2: ')))

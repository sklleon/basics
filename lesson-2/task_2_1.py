# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

new_list = [12, 9.52,'Games', True, None, [1,2,3,4,5]]
for i in new_list:
    print(f'Элемента списка {i} тип данных {type(i)}')

new_list.extend(input('Добавьте еще один элемент списка: '))
print(type(new_list[-1]))
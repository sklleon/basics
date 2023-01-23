# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

#  вариант 1
def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших позиционных аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('Аргумент 1-й: ')),
    int(input('Аргумент 2-й: ')),
    int(input('Аргумент 3-й: '))
)

#  вариант 2
# def my_func(a,b,c):
#     b_ar = 0
#     return b_ar
#
# line = (input('введите три числа' ).split())
# print(line)
# print(min(line))
# print(sum(line))
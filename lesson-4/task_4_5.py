# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
from itertools import count


# version 1
def generator():
    for el in range(100, 1001, 2):
        yield el


g = generator()


def my_func(prev_el, g):
    return prev_el * g


print(reduce(my_func, g))

# version 2
my_list = [el for el in range(100, 1001) if el % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, my_list))

# version 3
# my_list2 = [el for el in count(100) if el % 2 == 0 and el < 1001]
#
#
# def my_func2(prev_el, el):
#     return prev_el * el
# print(reduce(my_func2, my_list2))

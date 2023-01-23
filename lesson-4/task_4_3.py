# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.

# version 1
from itertools import count

new_list = []
for el in count(20):
    if el > 240:
        break
    else:
        if el % 20 == 0 or el % 21 == 0:
            new_list.append(el)
print(new_list)

# version 2
num = range(20, 241)
new_list = [el for el in num if el % 20 == 0 or el % 21 == 0]
print(new_list)

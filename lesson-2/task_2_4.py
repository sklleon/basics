# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

my_string = input('Введите строку из нескольких слов: ')
my_word = []
number = 1
for i in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f' {number} {my_word[i]}')
        number += 1
    else:
        print(f' {number} {my_word[i][0:10]}')
        number += 1

# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

items_list = int(input("Введите количество элементов списка: "))
my_list = []
i = 0
element = 0

while i < items_list:
    my_list.append(input('Введите значение списка: '))
    i +=1
for b in range(int(len(my_list)/2)):
    my_list[element], my_list[element + 1] = my_list[element + 1], my_list[element]
    element += 2
print(my_list)
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

while True:
    your_number = int(input('Введите целое положительное число: '))
    if your_number < 0 or your_number % 2 != 0:
        print('Вы ввели не верное число:')
    else:
        break

max_number = 0
for i in range(your_number):
    if i % 2 == 0:
        max_number = i

print(f'Cамая большая цифра в числе: {max_number}.')
# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

entered_time = int(input('Введите время в секундах: '))
hours = entered_time // 3600
minutes = (entered_time % 3600) // 60
seconds = (entered_time % 3600) % 60
print(f'Перевел время в часы: {hours}, минуты: {minutes}, секунды: {seconds} и выведите в формате чч:мм:сс.: {hours}:{minutes}:{seconds}')
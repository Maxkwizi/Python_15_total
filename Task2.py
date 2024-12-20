# Задача 2. Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в формате YYYY-MM-DD HH:MM:SS. 
# Дополнительно, выведите день недели и номер недели в году

import datetime

# Получение текущее время и даты из системы
now = datetime.datetime.now()

# Формат даты и времени в представлении YYYY-MM-DD HH:MM:SS
formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

# Получение дня недели и номера недели в году
# Полное название дня недели
day_of_week = now.strftime('%A')
# Номер недели в году
week_number = now.isocalendar()[1]  

# Вывод всех данных времени в формате
print(f'Текущая дата и время: {formatted_datetime}')
print(f'День недели: {day_of_week}')
print(f'Номер недели в году: {week_number}')


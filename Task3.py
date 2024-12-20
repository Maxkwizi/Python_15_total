'''
Задача 3. Планирование задач
Напишите функцию, которая принимает количество дней от текущей даты и возвращает дату, 
которая наступит через указанное количество дней. 
Дополнительно,выведите эту дату в формате YYYY-MM-DD.
'''

import datetime

def get_future_date(days_ahead):
    # Получение текущей даты
    current_date = datetime.datetime.now()
    
    # Вычисление будущей даты
    future_date = current_date + datetime.timedelta(days=days_ahead)
    
    # Формат даты в виде YYYY-MM-DD
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    
    return formatted_future_date


days_input = int(input("Введите количество дней: "))
future_date = get_future_date(days_input)
print(f"Дата через {days_input} дней: {future_date}")

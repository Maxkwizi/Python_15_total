'''
Задача 4. Опции и флаги
Напишите скрипт, который принимает два аргумента командной строки: число и строку. 
Добавьте следующие опции:
--verbose, если этот флаг установлен, скрипт должен выводить дополнительную информацию о процессе.
--repeat, если этот параметр установлен, он должен указывать, сколько раз повторить строку в выводе.
'''

import argparse

def main(number, string, repeat, verbose):
    if verbose:
        print(f"Получено число: {number}")
        print(f"Получена строка: '{string}'")
        print(f"Количество повторений: {repeat}")

    # Повторение строки указанное количество раз
    output = (string + ' ') * repeat
    

    print(f"Результат: {output}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description ="Обработка числа и строки.")

    # Добавляем аргумент для числа
    parser.add_argument("number", type = int, help="Целое число")
    # Добавляем аргумент для строки
    parser.add_argument("string", type = str, help="Строка для повторения")
    # Добавляем опцию для verbose
    parser.add_argument("--verbose", action ="store_true", help ="Выводит дополнительную информацию о процессе")
    # Добавляем опцию для указания количества повторов
    parser.add_argument("--repeat", type = int, default = 1, help ="Количество повторений строки")

    # Парсим аргументы
    args = parser.parse_args()

    # Вызываем главную функцию с полученными аргументами
    main(args.number, args.string, args.repeat, args.verbose)

'''
Команды для запуска скрипта в консоли:
    python Task4.py "Слово для вывода" 
    python Task4.py 23, "Слово для вывода" --verbose
    python Task4.py 4, "Слово для вывода" --repeat
'''
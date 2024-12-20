'''
Задача 5. Запуск из командной строки
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. 
Соберите информацию о содержимом в виде объектов namedtuple. 
Каждый объект хранит: имя файла без расширения или название каталога, расширение, 
если это файл, флаг каталога, название родительского каталога. 
В процессе сбора сохраните данные в текстовый файл используя логирование.
'''

import os
import logging
from collections import namedtuple
import argparse

# Определение конфигурации логирования
logging.basicConfig(filename='directory_contents.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Установка объекта namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', 'name extension is_directory parent_directory')

def collect_directory_info(directory):
    contents = []
    for entry in os.scandir(directory):
        if entry.is_file():
            name, extension = os.path.splitext(entry.name)
            is_directory = False
        elif entry.is_dir():
            name = entry.name
            extension = None
            is_directory = True
        else:
            continue
        
        parent_directory = os.path.basename(directory)
        file_info = FileInfo(name, extension, is_directory, parent_directory)
        contents.append(file_info)
        
        # Логирование информации
        logging.info(f'Collected: {file_info}')
    
    return contents

def main(directory):
    if not os.path.isdir(directory):
        print(f'Ошибка: {directory} не является директорией.')
        return
    
    contents = collect_directory_info(directory)
    print(f'Содержимое директории {directory}:')
    for info in contents:
        print(info)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description ='Собрать информацию о содержимом директории.')
    parser.add_argument('directory', type=str, help ='Путь до директории')
    args = parser.parse_args()
    
    main(args.directory)

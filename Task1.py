'''
Задание 1. Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
WARNING и выше — в warnings_errors.log.
'''

import logging

# Создание логера
logger = logging.getLogger('Logger_levels')

# Минимальный уровень логирования DEBUG
logger.setLevel(logging.DEBUG)

# Обработка логов уровней DEBUG и INFO с использованием FileHandler

# Указание файла для созранения логов уровня DEBUG
debug_info_handler = logging.FileHandler('debug_info.log')
# Установка уровня логирования
debug_info_handler.setLevel(logging.DEBUG)
# Создание объекта для определения формата сообщений
debug_info_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# Метод форматирования для обработчиков
debug_info_handler.setFormatter(debug_info_formatter)

# Обработка логов уровней WARNING и выше
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
warnings_errors_handler.setFormatter(warnings_errors_formatter)

# Добавление обработчиков в логгер
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Сообщения логов по всем уровням
logger.debug('1 level message DEBUG')
logger.info('2 level message INFO')
logger.warning('3 level message WARNING')
logger.error('4 level message ERROR')
logger.critical('5 level message CRITICAL')

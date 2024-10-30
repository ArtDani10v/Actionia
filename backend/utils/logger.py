# backend/utils/logger.py

import logging
import os
from datetime import datetime

# Определение пути к логам
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, 'backend.log')

# Создание логгера
logger = logging.getLogger('ActioniaLogger')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Создание обработчика для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Создание формата логов
formatter = logging.Formatter(
    fmt='%(asctime)s / %(levelname)s / %(funcName)s / %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_info(message, function='General'):
    """
    Логирование информационных сообщений.
    """
    logger.info(f"{function} - {message}")

def log_error(message, function='General'):
    """
    Логирование ошибок.
    """
    logger.error(f"{function} - {message}")

def log_debug(message, function='General'):
    """
    Логирование отладочных сообщений.
    """
    logger.debug(f"{function} - {message}")

def log_critical(message, function='General'):
    """
    Логирование критических сообщений.
    """
    logger.critical(f"{function} - {message}")

if __name__ == "__main__":
    # Пример использования логгера
    log_info("Тестовое информационное сообщение.", "TestFunction")
    log_error("Тестовое сообщение об ошибке.", "TestFunction")
    log_debug("Тестовое отладочное сообщение.", "TestFunction")
    log_critical("Тестовое критическое сообщение.", "TestFunction")

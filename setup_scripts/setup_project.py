import os
from pathlib import Path

# Определение корневой директории проекта
project_root = Path(__file__).resolve().parent.parent

# Определение структуры каталогов
directories = [
    project_root / 'backend' / 'utils',
    project_root / 'backend' / 'functions',
    project_root / 'scripts' / 'ahk',
    project_root / 'logs',
    project_root / 'tests',
    project_root / 'setup_scripts',
    project_root / 'data' / 'articles',
    project_root / 'scripts' / 'python',
]

# Создание всех необходимых каталогов
for directory in directories:
    directory.mkdir(parents=True, exist_ok=True)
    print(f"Создана папка: {directory}")

# Функции для создания файлов с содержимым


def create_file(file_path, content):
    if not file_path.exists():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Создан файл: {file_path}")
    else:
        print(f"Файл уже существует: {file_path}")


# Создание файла .env
env_content = '''# backend/.env

DATABASE_URL=postgresql://user:password@localhost:5432/actionia_db
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
EMAIL_USER=your-email@example.com
EMAIL_PASSWORD=your-email-password
'''
create_file(project_root / '.env', env_content)

# Создание файла backend/app.py
app_py_content = '''# backend/app.py

from flask import Flask, request, jsonify
from utils.logger import log_info, log_error
from functions.middle_click import execute_middle_click
from functions.article_processing import process_article
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "Actionia Backend is Running."

@app.route('/click', methods=['POST'])
def click():
    """
    Эндпоинт для выполнения клика средней кнопкой мыши.
    """
    try:
        execute_middle_click()
        return jsonify({"status": "success", "message": "Middle click executed."}), 200
    except Exception as e:
        log_error(f"Ошибка в эндпоинте /click: {e}", "click")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/process_article', methods=['POST'])
def handle_article():
    """
    Эндпоинт для обработки артикула.
    Ожидает JSON с полем 'mode'.
    """
    data = request.get_json()
    mode = data.get('mode')
    if mode not in ['1', '2', '3', '4']:
        log_error(f"Неверный режим: {mode}", "handle_article")
        return jsonify({"status": "error", "message": "Invalid mode."}), 400
    try:
        process_article(mode)
        return jsonify({"status": "success", "message": f"Article processed in mode {mode}."}), 200
    except Exception as e:
        log_error(f"Ошибка в эндпоинте /process_article: {e}", "handle_article")
        return jsonify({"status": "error", "message": str(e)}), 500

def main():
    """
    Основная функция для запуска Flask-приложения.
    """
    app.run(debug=True)

if __name__ == '__main__':
    main()
'''
create_file(project_root / 'backend' / 'app.py', app_py_content)

# Создание файла backend/utils/logger.py
logger_py_content = '''# backend/utils/logger.py

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
'''
create_file(project_root / 'backend' / 'utils' /
            'logger.py', logger_py_content)

# Создание файлов backend/functions/__init__.py
create_file(project_root / 'backend' / 'functions' / '__init__.py', '')

# Создание файлов backend/utils/__init__.py
create_file(project_root / 'backend' / 'utils' / '__init__.py', '')

# Создание файла backend/functions/middle_click.py
middle_click_py_content = '''# backend/functions/middle_click.py

import subprocess
from utils.logger import log_info, log_error
import os

def execute_middle_click():
    """
    Выполняет клик средней кнопкой мыши через AHK-скрипт.
    """
    # Определение пути к AHK-скрипту
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ahk_script_path = os.path.join(current_dir, '..', '..', 'scripts', 'ahk', 'middle_click.ahk')

    try:
        # Запуск AHK-скрипта
        subprocess.run(['AutoHotkey.exe', str(ahk_script_path)], check=True)
        log_info("Выполнен клик средней кнопкой мыши.", "execute_middle_click")
    except subprocess.CalledProcessError as e:
        log_error(f"Ошибка при выполнении middle_click.ahk: {e}", "execute_middle_click")
    except FileNotFoundError:
        log_error("AutoHotkey.exe не найден. Убедитесь, что AutoHotkey установлен и добавлен в PATH.", "execute_middle_click")
'''
create_file(project_root / 'backend' / 'functions' /
            'middle_click.py', middle_click_py_content)

# Создание файла backend/functions/article_processing.py
article_processing_py_content = '''# backend/functions/article_processing.py

import subprocess
from utils.logger import log_info, log_error
import os

def process_article(mode):
    """
    Обрабатывает артикул в зависимости от выбранного режима.
    :param mode: Режим обработки (1, 2, 3, 4)
    """
    # Определение пути к AHK-скрипту
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ahk_script_path = os.path.join(current_dir, '..', '..', 'scripts', 'ahk', 'article_processing.ahk')

    try:
        # Запуск AHK-скрипта с аргументом mode
        subprocess.run(['AutoHotkey.exe', str(ahk_script_path), str(mode)], check=True)
        log_info(f"Обработка артикула в режиме {mode}.", "process_article")
    except subprocess.CalledProcessError as e:
        log_error(f"Ошибка при обработке артикула: {e}", "process_article")
    except FileNotFoundError:
        log_error("AutoHotkey.exe не найден. Убедитесь, что AutoHotkey установлен и добавлен в PATH.", "process_article")
'''
create_file(project_root / 'backend' / 'functions' /
            'article_processing.py', article_processing_py_content)

# Создание файла backend/requirements.txt
requirements_txt_content = '''flask==2.0.3
python-dotenv==0.19.2
'''
create_file(project_root / 'backend' /
            'requirements.txt', requirements_txt_content)

# Создание файла backend/setup.py
setup_py_content = '''# backend/setup.py

from setuptools import setup, find_packages

setup(
    name="Actionia",  # Имя проекта
    version="0.1",  # Начальная версия
    author="ArtDani10v",  # Имя разработчика
    author_email="artdanilovru@gmail.com",  # Электронная почта
    description="Инновационный проект для автоматизации бизнес процессов",
    packages=find_packages(),  # Автоматически находит и добавляет все пакеты
    install_requires=[
        'flask==2.0.3',
        'python-dotenv==0.19.2',
    ],  # Здесь мы можем указать зависимости (если есть)
)
'''
create_file(project_root / 'backend' / 'setup.py', setup_py_content)

# Создание AHK скриптов
# Файл scripts/ahk/middle_click.ahk
middle_click_ahk_content = '''; scripts/ahk/middle_click.ahk

#Persistent
#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

; Горячая клавиша для выполнения клика средней кнопкой мыши
^!c:: ; Ctrl + Alt + C
    Click, Middle
    LogAction("Выполнен клик средней кнопкой мыши.", "INFO", "MiddleClick")
    return

; Функция для логирования через Python
LogAction(Message, Status, Function) {
    ; Определение пути к Python-скрипту логирования
    logger_script := "../../backend/utils/logger.py"
    ; Формирование команды для запуска Python-скрипта
    RunWait, "python.exe" "%logger_script%" "%Message%" "%Status%" "%Function%", , Hide
}
'''
create_file(project_root / 'scripts' / 'ahk' /
            'middle_click.ahk', middle_click_ahk_content)

# Файл scripts/ahk/article_processing.ahk
article_processing_ahk_content = '''; scripts/ahk/article_processing.ahk

#Persistent
#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

; Горячая клавиша для запуска обработки артикулов
^!a:: ; Ctrl + Alt + A
    ; Получение режима обработки через InputBox
    InputBox, mode, Выбор Режима, Введите режим обработки (1, 2, 3, 4):
    if (ErrorLevel) {
        LogAction("Ввод режима отменен пользователем.", "INFO", "ArticleProcessing")
        return
    }

    ; Запуск обработки артикула с выбранным режимом
    RunWait, "python.exe" "../../backend/functions/article_processing.py" "%mode%", , Hide
    LogAction("Запущена обработка артикула в режиме " . mode, "INFO", "ArticleProcessing")
    return

; Функция для логирования через Python
LogAction(Message, Status, Function) {
    ; Определение пути к Python-скрипту логирования
    logger_script := "../../backend/utils/logger.py"
    ; Формирование команды для запуска Python-скрипта
    RunWait, "python.exe" "%logger_script%" "%Message%" "%Status%" "%Function%", , Hide
}
'''
create_file(project_root / 'scripts' / 'ahk' /
            'article_processing.ahk', article_processing_ahk_content)

# Создание тестовых файлов
# Файл tests/test_logger.py
test_logger_py_content = '''# tests/test_logger.py

import os
import sys
import pytest

# Добавление пути к backend для импорта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from utils.logger import log_info, log_error, LOG_FILE

def test_log_info():
    log_info("Тестовое информационное сообщение.", "TestFunction")
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        logs = f.read()
    assert "TestFunction - Тестовое информационное сообщение." in logs

def test_log_error():
    log_error("Тестовое сообщение об ошибке.", "TestFunction")
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        logs = f.read()
    assert "TestFunction - Тестовое сообщение об ошибке." in logs
'''
create_file(project_root / 'tests' / 'test_logger.py', test_logger_py_content)

# Файл tests/test_functions.py
test_functions_py_content = '''# tests/test_functions.py

import os
import sys
import pytest
from unittest.mock import patch, MagicMock

# Добавление пути к backend для импорта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from functions.middle_click import execute_middle_click
from functions.article_processing import process_article

@patch('functions.middle_click.subprocess.run')
@patch('functions.middle_click.log_info')
def test_execute_middle_click(mock_log_info, mock_subprocess_run):
    execute_middle_click()
    mock_subprocess_run.assert_called_once_with(['AutoHotkey.exe', '../../scripts/ahk/middle_click.ahk'], check=True)
    mock_log_info.assert_called_with("Выполнен клик средней кнопкой мыши.", "execute_middle_click")

@patch('functions.article_processing.subprocess.run')
@patch('functions.article_processing.log_info')
def test_process_article(mock_log_info, mock_subprocess_run):
    process_article('1')
    mock_subprocess_run.assert_called_once_with(['AutoHotkey.exe', '../../scripts/ahk/article_processing.ahk', '1'], check=True)
    mock_log_info.assert_called_with("Обработка артикула в режиме 1.", "process_article")
'''
create_file(project_root / 'tests' / 'test_functions.py',
            test_functions_py_content)

# Создание файла data/articles/sample_article.txt
sample_article_txt_content = '''ART123456
'''
create_file(project_root / 'data' / 'articles' /
            'sample_article.txt', sample_article_txt_content)

# Создание файла scripts/python/requirements.txt
python_scripts_requirements_content = '''# scripts/python/requirements.txt

pyperclip==1.8.2
'''
create_file(project_root / 'scripts' / 'python' /
            'requirements.txt', python_scripts_requirements_content)

print("\n✅ Установочный скрипт успешно создал всю необходимую структуру проекта и базовые файлы, исключив LICENSE и README.md.")
print("Теперь вы можете перейти к установке зависимостей и запуску проекта.")

import os
from unittest.mock import patch
from backend.functions.middle_click import execute_middle_click
from backend.functions.article_processing import process_article
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()
BASE_PROJECT_PATH = os.getenv("PROJECT_BASE_PATH")


@patch('backend.functions.middle_click.subprocess.run')
@patch('backend.functions.middle_click.log_info')
def test_execute_middle_click(mock_log_info, mock_subprocess_run):
    # Формируем ожидаемый путь к скрипту аналогично коду функции
    expected_path = os.path.join(
        BASE_PROJECT_PATH, 'scripts', 'ahk', 'middle_click.ahk')

    # Вызов тестируемой функции
    execute_middle_click()

    # Проверка, что subprocess.run был вызван с правильными аргументами
    mock_subprocess_run.assert_called_once_with(
        ['AutoHotkey.exe', expected_path], check=True)


@patch('backend.functions.article_processing.subprocess.run')
@patch('backend.functions.article_processing.log_info')
def test_process_article(mock_log_info, mock_subprocess_run):
    # Формируем ожидаемый путь к скрипту аналогично коду функции
    expected_path = os.path.join(
        BASE_PROJECT_PATH, 'scripts', 'ahk', 'article_processing.ahk')

    # Вызов тестируемой функции
    process_article('1')

    # Проверка, что subprocess.run был вызван с правильными аргументами
    mock_subprocess_run.assert_called_once_with(
        ['AutoHotkey.exe', expected_path, '1'], check=True)

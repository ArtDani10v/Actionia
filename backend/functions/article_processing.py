# backend/functions/article_processing.py

import os
import subprocess
from utils.logger import log_info, log_error
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()
BASE_PROJECT_PATH = os.getenv("PROJECT_BASE_PATH")


def process_article(article_id):
    """
    Выполняет обработку артикула через AHK-скрипт.
    """
    ahk_script_path = os.path.join(
        BASE_PROJECT_PATH, 'scripts', 'ahk', 'article_processing.ahk')

    try:
        subprocess.run(
            ['AutoHotkey.exe', ahk_script_path, article_id], check=True)
        log_info(f"Обработка артикула {
                 article_id} выполнена.", "process_article")
    except subprocess.CalledProcessError as e:
        log_error(f"Ошибка при выполнении article_processing.ahk: {
                  e}", "process_article")
    except FileNotFoundError:
        log_error(
            "AutoHotkey.exe не найден. Убедитесь, что AutoHotkey установлен и добавлен в PATH.", "process_article")

import os
import subprocess
from utils.logger import log_info, log_error
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()
BASE_PROJECT_PATH = os.getenv("PROJECT_BASE_PATH")


def execute_middle_click():
    """
    Выполняет клик средней кнопкой мыши через AHK-скрипт.
    """
    ahk_script_path = os.path.join(
        BASE_PROJECT_PATH, 'scripts', 'ahk', 'middle_click.ahk')

    try:
        subprocess.run(['AutoHotkey.exe', ahk_script_path], check=True)
        log_info("Выполнен клик средней кнопкой мыши.", "execute_middle_click")
    except subprocess.CalledProcessError as e:
        log_error(f"Ошибка при выполнении middle_click.ahk: {
                  e}", "execute_middle_click")
    except FileNotFoundError:
        log_error("AutoHotkey.exe не найден. Убедитесь, что AutoHotkey установлен и добавлен в PATH.",
                  "execute_middle_click")

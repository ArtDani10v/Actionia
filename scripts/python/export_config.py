import os
from backend.utils.config import BASE_PATH, EXCEL_FILE_PATH, COPY_TEMPLATE, MOUSE_DELAY, DIALOG_TIMEOUT

# Определение настроек и комментариев для каждой переменной
settings = {
    "AHK_BASE_PATH": (BASE_PATH, "; BASE_PATH формируем гибкий путь к папке с проектом"),
    "AHK_EXCEL_FILE_PATH": (EXCEL_FILE_PATH, "; EXCEL_FILE_PATH формируем гибкий путь к файлам с таблицами"),
    "FolderPathAhk": ('AHK_BASE_PATH . "\\scripts\\ahk"', "; формируем гибкий путь к файлам AHK"),
    "FolderOptionalWb": ('AHK_BASE_PATH . "\\src\\optional\\wb\\"', "; D:\\Projects\\Actionia\\src\\optional\\wb"),
    "FolderOptionalOz": ('AHK_BASE_PATH . "\\src\\optional\\oz\\"', "; D:\\Projects\\Actionia\\src\\optional\\oz"),
    "CopyTemplate": (COPY_TEMPLATE, "; COPY_TEMPLATE добавления гибкого имени файлов"),
    "MouseDelay": (MOUSE_DELAY, "; MOUSE_DELAY Указываем скорость"),
    "DialogTimeout": (DIALOG_TIMEOUT, "; DIALOG_TIMEOUT Указываем таймаут")
}


def load_existing_config(ahk_config_path):
    """Чтение существующего файла config.ahk в словарь."""
    config_data = {}
    if os.path.exists(ahk_config_path):
        with open(ahk_config_path, "r", encoding="utf-8") as file:
            for line in file:
                # Пропускаем комментарии и пустые строки
                if line.strip().startswith(";") or not line.strip():
                    continue
                # Разбиваем строку на переменную и значение
                if ":=" in line:
                    name, value = line.split(":=", 1)
                    config_data[name.strip()] = value.strip()
    return config_data


def update_config(ahk_config_path):
    """Обновление config.ahk с учетом значений из config.py."""
    # Загружаем существующие переменные из config.ahk
    existing_config = load_existing_config(ahk_config_path)

    # Новый контент для записи в файл
    new_content = []

    # Обрабатываем каждую настройку из config.py
    for name, (value, comment) in settings.items():
        if isinstance(value, str) and not value.startswith('AHK_BASE_PATH'):
            value = f'"{value}"'
        line = f'global {name} := {value} {comment}\n'

        # Если переменная уже существует и значение отличается, обновляем её
        if name in existing_config:
            if existing_config[name] != value:
                new_content.append(line)  # Обновляем значение
        else:
            # Если переменной нет, добавляем её в начало
            new_content.append(line)

    # Читаем весь оригинальный файл, оставляя неизменные строки
    if os.path.exists(ahk_config_path):
        with open(ahk_config_path, "r", encoding="utf-8") as file:
            existing_lines = file.readlines()
    else:
        existing_lines = []

    # Сохраняем все строки, кроме тех, которые уже были добавлены или обновлены
    for line in existing_lines:
        if not any(line.startswith(f"global {name}") for name in settings.keys()):
            new_content.append(line)

    # Записываем новый контент в файл
    with open(ahk_config_path, "w", encoding="utf-8") as file:
        file.writelines(new_content)

    print(f"Конфигурация экспортирована в {ahk_config_path}")


# Запуск функции экспорта
if __name__ == "__main__":
    ahk_config_path = os.path.join("scripts", "ahk", "config.ahk")
    update_config(ahk_config_path)

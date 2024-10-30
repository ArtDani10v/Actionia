; Устанавливаем глобальный путь для файла с логами
LogAction(Message := "", Status := "INFO", Action := "General") {
    global ProjectPath
    IniFilePath := ProjectPath . "\src\logs\log.txt"  ; Формируем путь к лог-файлу

    ; Проверка, установлен ли путь к файлу лога
    if (IniFilePath = "") {
        MsgBoxWithTimeout("Ошибка: Путь к лог-файлу не определён!", 5)
        return
    }

    ; Проверка существования директории
    SplitPath, IniFilePath, , Dir
    if (!FileExist(Dir)) {
        MsgBoxWithTimeout("Папка для лог-файла не существует: " . Dir, 5)
        FileCreateDir, %Dir%
        if (ErrorLevel) {
            MsgBoxWithTimeout("Ошибка: Не удалось создать директорию: " . Dir, 5)
            return
        }
    }

    ; Получаем текущие дату и время
    CurrentTime := A_Hour ":" A_Min ":" A_Sec
    CurrentDate := A_YYYY "-" A_MM "-" A_DD

    ; Формируем строку для логирования
    LogEntry := CurrentDate " / " CurrentTime " / " Status " / " Action " / " Message

    ; Записываем в лог-файл
    FileAppend, %LogEntry%`n, %IniFilePath%
    if (ErrorLevel) {
        MsgBoxWithTimeout("Ошибка: Не удалось записать лог в файл: " . IniFilePath, 5)
    } else {
        ; Для отладки можно добавить опциональное сообщение об успешной записи
        ; MsgBoxWithTimeout("Лог успешно записан", 3)  ; Уберите комментарий, если нужно
    }
}

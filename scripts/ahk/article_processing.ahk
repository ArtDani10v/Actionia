; scripts/ahk/article_processing.ahk

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

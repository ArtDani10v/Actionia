; scripts/ahk/middle_click.ahk

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

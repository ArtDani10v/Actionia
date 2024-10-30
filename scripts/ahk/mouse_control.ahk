; Функция для управления действиями мыши
HandleMButtonClick(keypressDuration, activeProcess, x := "", y := "") {
    global MouseDelay, AppActions  ; Используем глобальные переменные для задержки и действий

    ; Логируем событие клика
    LogAction("Нажата средняя кнопка мыши в " . activeProcess . " с длительностью " . keypressDuration . " мс", "INFO", "MouseControl")

    ; Определяем поведение в зависимости от продолжительности нажатия
    if (keypressDuration < MouseDelay) {
        ; Ищем совпадение части имени процесса и вызываем соответствующее действие
        for app, action in AppActions {
            if (InStr(activeProcess, app)) {
                if IsFunc(action) {
                    ;MsgBoxWithTimeout("Щелкните левой кнопкой мыши, чтобы захватить координаты.", 3)
                    action.Call(x, y)  ; Вызов функции действия с координатами
                    ;KeyWait, LButton, D  ; Ожидаем нажатия левой кнопки мыши
                    MouseGetPos, x, y  ; Получаем координаты мыши после клика
                    LogAction("Координаты клика: X: " . x . " Y: " . y, "INFO", "MouseControl")

                } else {
                    LogAction("Ошибка: Действие для " . app . " не является функцией.", "ERROR", "MouseControl")
                }
                return
            }
        }

        ; Стандартное действие, если приложение не найдено
        MsgBoxWithTimeout("Вы нажали мышку в нераспознанном приложении")
    } else {
        ; Долгое нажатие
        MsgBoxWithTimeout("Долгое нажатие мышки")
        ; Вызываем функцию с параметрами
        HandleMButtonClick(100, activeProcess, 200, 200)
    }
}





HandleMButtonClick2(keypressDuration, activeProcess) {
    global MouseDelay, AppActions  ; Используем настройки из config.ahk

    ; Определяем поведение в зависимости от продолжительности нажатия
    if (keypressDuration < MouseDelay) {
        ; Ищем совпадение части имени процесса
        for app, action in AppActions {
            if (InStr(activeProcess, app)) {
                action.Call()  ; Вызов функции действия
                return
            }
        }

        ; Стандартное действие, если приложение не найдено
        MsgBoxWithTimeout("Вы нажали мышку в нераспознанном приложении")
    } else {
        ; Долгое нажатие
        MsgBoxWithTimeout("Долгое нажатие мышки")
    }
    ; Если переданы координаты, можем кликнуть на заданных x, y
    if (x != "" && y != "") {
        MouseClick, L, %x%, %y%
    }


}


; Функция для отображения сообщения с тайм-аутом
MsgBoxWithTimeout(message, timeout := "") {
    global DialogTimeout

    ; Если тайм-аут не передан, используем значение из конфигурации
    if (timeout = "") {
        timeout := DialogTimeout
    }

    ; Логируем вызов MsgBox
    LogAction("Вызван MsgBoxWithTimeout с сообщением: " . message . " и тайм-аутом: " . timeout, "INFO", "DialogUtils")

    ; Если тайм-аут больше 0, устанавливаем таймер для автоматического закрытия
    if (timeout > 0) {
        SetTimer, CloseMsgBox, -%timeout%000  ; Запускаем таймер на закрытие через указанный тайм-аут
        MsgBox, %message%  ; Показываем диалоговое окно
    } else {
        ; Если тайм-аут не указан или равен 0, ждём нажатия "OK"
        MsgBox, %message%
    }
}

; Лейбл для автоматического закрытия MsgBox
CloseMsgBox:
    WinClose, ahk_class #32770  ; Закрываем диалоговое окно по классу окна

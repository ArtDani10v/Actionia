; Действие для проводника с кликом по координатам или обычным кликом
ActionExplorer(x := "", y := "") {
    try {
        LogAction("Выполнение действия ActionExplorer", "INFO", "Actions")

        ; Если переданы координаты, выполняем клик на указанных x, y, иначе просто клик
        if (x != "" && y != "") {
            MouseClick, L, %x%, %y%
            LogAction("Выполнен клик по координатам: X: " . x . " Y: " . y, "INFO", "Actions")
        } else {
            Click  ; Обычный клик
            LogAction("Выполнен обычный клик.", "INFO", "Actions")
        }

        ; Продолжаем работу с буфером обмена
        var := Clipboard := ""
        Send, ^{vk43}  ; Копирование содержимого в буфер обмена
        ClipWait, 1  ; Ожидаем максимум 1 секунду

        ; Проверяем, пуст ли буфер обмена
        if (Clipboard = "") {
            LogAction("Ошибка: Буфер обмена пуст. Нет данных для копирования.", "ERROR", "Clipboard")
            ;MsgBoxWithTimeout("Буфер обмена пуст. Операция не может быть завершена.")
            return
        }

        ; Обрабатываем данные из буфера обмена
        Loop, Parse, Clipboard, `n, `r
        {
            SplitPath, A_LoopField,,,,fileNameNoEXT
            var .= fileNameNoExt
        }

        Article := var
        global FolderArticle := Folder
        LogAction("Получен артикул через буфер обмена: " . Article, "INFO", "Clipboard")

    } catch e {
        LogAction("Ошибка в ActionExplorer: " . e.Message, "ERROR", "Actions")
        MsgBoxWithTimeout("Произошла ошибка: " . e.Message)
    }
}




; Функция для Photoshop
ActionPhotoshop() {
    try {
        LogAction("Выполнение действия Photoshop", "INFO", "Actions")
        ; Действие Photoshop
    } catch e {
        LogAction("Ошибка в ActionPhotoshop: " . e.Message, "ERROR", "Actions")
        MsgBoxWithTimeout("Произошла ошибка: " . e.Message)
    }
}

; Функция для Figma
ActionFigma() {
    try {
        LogAction("Выполнение действия Figma", "INFO", "Actions")
        ; Действие Figma
    } catch e {
        LogAction("Ошибка в ActionFigma: " . e.Message, "ERROR", "Actions")
        MsgBoxWithTimeout("Произошла ошибка: " . e.Message)
    }
}

; Функция для CorelDRAW
ActionCorel() {
    try {
        LogAction("Выполнение действия CorelDRAW", "INFO", "Actions")
        ; Действие Figma
    } catch e {
        LogAction("Ошибка в ActionCorelDRAW: " . e.Message, "ERROR", "Actions")
        MsgBoxWithTimeout("Произошла ошибка: " . e.Message)
    }
}


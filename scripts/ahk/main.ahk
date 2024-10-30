#Include includes.ahk  ; Подключаем файл со всеми includes

; Начальная инициализация
F12:: Suspend
Return
F11:: Reload
Return

; Пример вызова функции при нажатии F10 для тестирования настроек магазина
F10::
    ; Логируем событие клика
    LogAction("Нажата кнопка F10" . activeProcess . " с длительностью " . keypressDuration . " мс", "INFO", "MouseControl")

    ; Переменные для хранения значений настроек
    ShopName := ""
    Category := ""
    Marketplace := ""
    ProductCode := ""
    Files := ""

    ; Вызываем функцию чтения настроек для магазина "wb Автолегион"
if (ReadShopSettings("wb_Avtologion", ShopName, Category, Marketplace, ProductCode, Files)) {
    MsgBoxWithTimeout("Магазин: " . ShopName . "`nКатегория: " . Category . "`nМаркетплейс: " . Marketplace . "`nКод товара: " . ProductCode . "`nДоп. файлы: " . Files, 1)
} else {
    MsgBoxWithTimeout("Ошибка при чтении настроек магазина.")
}


return

$MButton::
    startTime := A_TickCount
    KeyWait, MButton, U
    keypressDuration := A_TickCount - startTime

    ; Получаем активное окно
    WinGet, activeProcess, ProcessName, A

; Вызываем функцию с параметрами
    HandleMButtonClick(keypressDuration, activeProcess)

return


; shop_settings.ahk
; Чтение настроек для указанного магазина
ReadShopSettings(shopName, ByRef shopTitle, ByRef category, ByRef marketplace, ByRef productCode, ByRef files) {
    global ProjectPath
    IniFilePath := ProjectPath . "\shop\shop.ini"  ; Формируем путь к INI-файлу

    ; Проверяем существование INI-файла
    if (!FileExist(IniFilePath)) {
        LogAction("Ошибка: INI-файл не найден: " . IniFilePath, "ERROR", "ShopSettings")
        MsgBoxWithTimeout("Ошибка: INИ-файл не найден по пути " . IniFilePath)
        return false
    }

    LogAction("Чтение INI-файла: " . IniFilePath, "INFO", "ShopSettings")
    LogAction("Читаем настройки для магазина: " . shopName, "INFO", "ShopSettings")

    ; Чтение параметров для указанного магазина
    IniRead, shopTitle, %IniFilePath%, %shopName%, shop_name, ERROR
    IniRead, category, %IniFilePath%, %shopName%, shop_category, ERROR
    IniRead, marketplace, %IniFilePath%, %shopName%, shop_marketplace, ERROR
    IniRead, productCode, %IniFilePath%, %shopName%, shop_product_code, ERROR
    IniRead, files, %IniFilePath%, %shopName%, shop_extra_files, ERROR

    ; Проверка на наличие ошибок при чтении
    if (shopTitle = "ERROR" || category = "ERROR" || marketplace = "ERROR" || productCode = "ERROR" || files = "ERROR") {
        LogAction("Ошибка: Не удалось прочитать настройки для магазина " . shopName, "ERROR", "ShopSettings")
        MsgBoxWithTimeout("Ошибка при чтении настроек для магазина: " . shopName)
        return false
    }

    LogAction("Настройки для магазина " . shopName . " успешно прочитаны", "INFO", "ShopSettings")
    return true
}




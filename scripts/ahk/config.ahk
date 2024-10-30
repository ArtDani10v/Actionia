global AHK_BASE_PATH := "D:/Projects/Actionia" ; BASE_PATH формируем гибкий путь к папке с проектом
global AHK_EXCEL_FILE_PATH := "C:/path/to/excel.xlsx" ; EXCEL_FILE_PATH формируем гибкий путь к файлам с таблицами
global FolderPathAhk := AHK_BASE_PATH . "\scripts\ahk" ; формируем гибкий путь к файлам AHK
global FolderOptionalWb := AHK_BASE_PATH . "\src\optional\wb\" ; D:\Projects\Actionia\src\optional\wb
global FolderOptionalOz := AHK_BASE_PATH . "\src\optional\oz\" ; D:\Projects\Actionia\src\optional\oz
global CopyTemplate := "image_{num}.png" ; COPY_TEMPLATE добавления гибкого имени файлов
global MouseDelay := 300 ; MOUSE_DELAY Указываем скорость
global DialogTimeout := 2 ; DIALOG_TIMEOUT Указываем таймаут
; config.ahk







; Настройки для действий в различных приложениях
; Получение AppActions тоже было бы удобно получать в зависимости от функций в action
global AppActions := {}

; Добавляем приложения и их действия (ссылки на функции в actions.ahk)
AppActions["explorer"] := Func("ActionExplorer")
AppActions["photoshop"] := Func("ActionPhotoshop")
AppActions["figma"] := Func("ActionFigma")
AppActions["coreldraw"] := Func("ActionCorel")

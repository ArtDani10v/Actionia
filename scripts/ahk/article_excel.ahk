GetArticleFromExcel(ExcelFilePath) {
    ; Проверяем, существует ли файл Excel
    if (!FileExist(ExcelFilePath)) {
        MsgBoxWithTimeout("Файл Excel не найден: " . ExcelFilePath)
        LogAction("Файл Excel не найден: " . ExcelFilePath, "ERROR", "ExcelNotFound")
        return
    }

    ; Получаем имя файла для логирования
    SplitPath, ExcelFilePath, FileName  ; Получаем только имя файла без пути

    ; Создаем объект Excel.Application
    xlApp := ComObjCreate("Excel.Application")
    xlApp.Visible := False  ; Скрываем Excel

    ; Открываем Excel-файл
    xlWorkbook := xlApp.Workbooks.Open(ExcelFilePath)

    ; Выбираем активный лист (в данном случае первый)
    xlSheet := xlWorkbook.Sheets(1)

    ; Получаем значение из первой ячейки, например
    Article := xlSheet.Cells(1, 1).Value

    ; Закрываем Excel
    xlWorkbook.Close()
    xlApp.Quit()

    ; Логируем обновление файла с использованием его имени
    LogAction("Файл Excel (" . FileName . ") обновлен: " . ExcelFilePath, "UPDATE", "ChanceArticle")

    return Article
}

; folder_management.ahk

CreateFolders(source) {
    if !source {
        InputBox, folderName, Введите название папки, Пожалуйста, введите название папки:
        if ErrorLevel {
            return
        }
    } else {
        folderName := source
    }

    targetPath := FolderPath "\" folderName
    FileCreateDir, %targetPath%

    LogAction("Создана папка: " targetPath)
    return targetPath
}

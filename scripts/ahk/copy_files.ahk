; copy_files.ahk

CopyFile(source, destination, article, num) {
    fileName := StrReplace(CopyTemplate, "{num}", Format("{:03}", num))
    newPath := destination "\" article "\" fileName

    FileCopy, %source%, %newPath%

    LogAction("Скопирован файл: " fileName " в " newPath)
}

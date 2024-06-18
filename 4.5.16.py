"""Наилучший показатель
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит название файла
из этого архива, который имеет наилучший показатель степени сжатия.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Гарантируется, что в исходном архиве только один файл имеет наилучший показатель степени сжатия.

Примечание 3. Степень сжатия файла характеризуется коэффициентом K, определяемым как отношение объема сжатого файла Vc к
объему исходного файла Vo, выраженным в процентах: K = Vc/Vo * 100%"""

from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    names = [info[i].filename.split('/')[-1] for i in range(len(info)) if info[i].is_dir() == False]
    sizes = [(100 - (info[i].compress_size / info[i].file_size) * 100) for i in range(len(info)) if info[i].is_dir() == False]
    mx, biggest = - 1, 0
    for i in range(len(names)):
        if sizes[i] > mx:
            mx, biggest = sizes[i], i
    print(names[biggest])
"""Избранные
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия файлов
из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия файлов должны быть расположены
в лексикографическом порядке, каждое на отдельной строке.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Начальная часть ответа выглядит так:

countries.json
data_sample.csv
..."""

from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    data = [info[i].filename.split('/')[-1] for i in range(len(info)) if info[i].is_dir() == False and info[i].date_time
            > (2021, 11, 30, 14, 22, 00)]
    print(*sorted(data, key=lambda x: x[0]), sep='\n')
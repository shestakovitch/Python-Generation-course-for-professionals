"""Разные типы
Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]
Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле
data.json, измененные по следующим правилам:

если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическим значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
если объект является пустым значением (null), он не добавляется
Полученный список программа должна записать в файл updated_data.json.

Примечание 1. Например, если бы файл data.json имел вид:

["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
то программа должна была бы создать файл updated_data.json со следующим содержанием:

["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]
Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8."""

import json

res = []
with open('data.json') as file:
    json_data = json.load(file)
    for item in json_data:
        if type(item) == str:
            res.append(item + '!')
        elif type(item) in (int, float):
            res.append(item + 1)
        elif type(item) == bool:
            res.append(not item)
        elif type(item) == list:
            res.append(item * 2)
        elif type(item) == dict:
            item.update({"newkey": None})
            res.append(item)
with open('updated_data.json', 'w') as out:
    json.dump(res, out)
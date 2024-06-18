"""Вам доступен словарь data. Дополните приведенный ниже код, чтобы он вывел данный словарь, расположив его элементы в
обратном порядке.

Примечание. Например, если бы словарь data имел вид:

data = OrderedDict(key1='value1', key2='value2', key3='value3')
то программа должна была бы вывести (до Python 3.12):

OrderedDict([('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1')])
в Python 3.12:

OrderedDict({('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1')})"""

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
print(OrderedDict(reversed(data.items())))
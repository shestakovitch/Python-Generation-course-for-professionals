"""Элементы JSON
Напишите программу, которая принимает на вход описание одного объекта в формате JSON и выводит все пары ключ-значение
этого объекта.

Формат входных данных
На вход программе подается корректное описание одного объекта в формате JSON.

Формат выходных данных
Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ и значение двоеточием, каждую на
отдельной строке. Если значением ключа является список, то все его элементы должны быть выведены через запятую.

Примечание 1. Пары ключ-значение при выводе должны располагаться в своем исходном порядке.

Примечание 2. Для считывания произвольного числа строк используйте потоковый ввод sys.stdin."""

import json
import sys

data = json.load(sys.stdin)
[print(f'{k}:', ", ".join(map(str, v)) if type(v) == list else v) for k, v in data.items()]
"""Одинаковые слоги
Напишите программу, которая выводит слова, состоящие из двух одинаковых слогов.

Формат входных данных
На вход программе подается произвольное количество слов, каждое на отдельной строке.

Формат выходных данных
Программа должна из введенных слов вывести только те, которые состоят из двух одинаковых слогов. Слова должны быть
расположены в своем исходном порядке, каждое на отдельной строке.

Примечание 1. Словом будем считать любую непрерывную последовательность из одного или нескольких символов,
соответствующих \w."""

import sys
from re import fullmatch

for item in [line.strip() for line in sys.stdin]:
    if fullmatch(r'^(\w+)\1$', item):
        print(item)
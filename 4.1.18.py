"""Гуру прогрессий
Дана последовательность целых чисел. Напишите программу, которая определяет, является ли данная последовательность
прогрессией, и если да, то определяет её вид.

Формат входных данных
На вход программе подается произвольное количество строк (не менее трёх), в каждой строке записано натуральное число —
очередной член последовательности.

Формат выходных данных
Программа должна вывести текст:

Арифметическая прогрессия, если введенная последовательность чисел является арифметической прогрессией
Геометрическая прогрессия, если введенная последовательность чисел является геометрической прогрессией
Не прогрессия, если введенная последовательность чисел не является прогрессией
Примечание 1. Гарантируется, что вид прогрессии определяется однозначно.

Примечание 2. Подробнее об арифметической и геометрической прогрессиях можно почитать тут и тут соответственно."""

import sys

data = [int(number) for number in sys.stdin]
dif_set = set([data[i + 1] - data[i] for i in range(len(data) - 1)])
div_set = set([data[i + 1] / data[i] for i in range(len(data) - 1)])
print('Арифметическая прогрессия' if len(dif_set) == 1 else 'Геометрическая прогрессия' if len(div_set) == 1
else 'Не прогрессия')
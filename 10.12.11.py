"""Перестановки
Напишите программу, которая выводит все перестановки символов строки без дубликатов.

Формат входных данных
На вход программе подается произвольная строка из строчных латинских букв, длина которой не превышает 10 символов.

Формат выходных данных
Программа должна вывести все перестановки символов данной строки без дубликатов в алфавитном порядке, каждую на
отдельной строке."""

from itertools import permutations

[print(*i, sep='') for i in sorted(set(permutations(input())))]
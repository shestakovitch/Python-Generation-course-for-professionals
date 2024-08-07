"""Одинаковые и разные 🍕
Американский английский и Британский английский языки имеют несколько различий, одно из которых наблюдается в написании
слов. Например, слова, написанные на Американском английском языке и имеющие суффикс ze, в Британском варианте языка
часто записываются с использованием суффикса se.

Напишите программу, которая определяет, сколько раз слово встречается в тексте, учитывая его Британско-Американское
написание.

Формат входных данных
На вход программе на первой строке подается слово, которое может быть записано как в Британском, так в Американском
варианте, а на следующей — текст.

Формат выходных данных
Программа должна определить, сколько раз введенное слово встречается в тексте, учитывая его Британско-Американское
написание, и вывести полученный результат.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами,
соответствующими \W.

Примечание 2. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми."""

import re

word, txt = input(), input()
print(len(re.findall(fr'\b({word[:-2]}[zs]e)\b', txt, re.I)))
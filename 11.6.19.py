"""Уважение
На электронную почту Тимура нередко приходят письма с предложением о сотрудничестве. Тимур ценит взаимное уважение и
считает письмо достойным внимания, если оно начинается с одного из следующих выражений:

Здравствуйте
Доброе утро
Добрый день
Добрый вечер
Напишите программу, которая определяет, является ли письмо достойным внимания Тимура.

Формат входных данных
На вход программе подается единственная строка .

Формат выходных данных
Программа должна вывести True, если введенная строка начинается с одного из представленных в условии задачи выражений
(в произвольном регистре), или False в противном случае."""

import re

print(bool(re.match(r'^(Здравствуйте)|(Доброе утро)|(Добрый день)|(Добрый вечер)', input(), re.I)))
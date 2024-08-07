"""Социальные сети
Вам доступен набор популярных публикаций из социальной сети Твиттер, которые могут иметь следующий вид:

Люблю курсы BEEGEEK!
Когда курс по ООП? @timur_guev
BEEGEEK, спасибо за курсы, вы лучшие! #python #BeeGeek
и т.д.
Напишите программу, которая определяет, в скольких публикациях содержится строка beegeek.

Формат входных данных
На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.

Формат выходных данных
Программа должна определить, в скольких введенных строках содержится строка beegeek в произвольном регистре, и вывести
полученный результат."""

import re

match = 0
for item in open(0): #[line.strip() for line in sys.stdin]:
    match += 1 if re.search(r'beegeek', item.strip(), re.I) else 0
print(match)
"""Булочный магнат
После ухода сети Макдональдс из России Тимур решил открыть свою небольшую бургерную. Цена каждого бургера в его
ресторане определяется количеством ингредиентов, которые выбирает сам посетитель. Вам доступны словари, в которых в
качестве ключа указано название ингредиента, а в качестве значения — его цена. Все ингредиенты разбиты по категориям,
например, овощи содержатся в одном словаре, соусы — в другом.

Напишите программу, которая принимает на вход ингредиенты, выбранные посетителем, и определяет их общую стоимость.

Формат входных данных
На вход программе подается последовательность ингредиентов, разделенных запятой без пробелов.

Формат выходных данных
Программа должна определить общую стоимость введенных ингредиентов и вывести полученный результат в виде чека, в котором
 указаны ингредиенты в лексикографическом порядке, количество каждых и их общая стоимость, в следующем формате:

<ингредиент 1> x <количество 1>
<ингредиент 2> x <количество 2>
...
-------------------------------
ИТОГ: <общая стоимость>р
Примечание 1. Программа должна добавлять нужное количество пробелов, если один ингредиент имеет меньшую длину, чем другие.

Примечание 2. Длина пунктирной линии должна равняться длине самой длинной строки в чеке, включая строку с итоговой стоимостью.

Примечание 3. Гарантируется, что все ингредиенты, выбранные посетителем, присутствуют в словарях."""

from collections import ChainMap
from collections import Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

burger_items = ChainMap(bread, meat, sauce, vegetables, toppings)
data = Counter(input().split(','))
n, s = len(max(data, key=len)), 0
for k, v in sorted(data.items(), key=lambda x: x[0]):
    print(f'{k:{n}} x {v}')
    s += v * burger_items[k]
total = f'ИТОГ: {s}р'
print('-' * (n + 3 + len(max(map(str, data.values())))) if (n + 3 + len(max(map(str, data.values())))) >= len(total)
      else '-' * len(total))
print(total)
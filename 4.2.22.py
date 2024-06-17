"""Голодный студент 🌶️
Дима очень хочет поесть, но денег у него мало. Помогите ему определить самый дешевый продукт, а также магазин, в котором
 он продается. Вам доступен файл prices.csv, который содержит информацию о ценах продуктов в различных магазинах. В
 первом столбце записано название магазина, а в последующих — цена на соответствующий товар в этом магазине:

Магазин;Творог;Гречка;Рис;Бородинский хлеб;Яблоки;Пельмени;Овсяное печенье;Спагетти;Печеная фасоль;Мороженое;Фарш;
Вареники;Картофель;Батончик
Пятерочка;69;133;129;83;141;90;72;123;149;89;88;106;54;84
Магнит;102;87;95;75;109;112;97;82;101;134;69;61;141;79
...
Напишите программу, которая определяет и выводит самый дешевый продукт и название магазина, в котором он продается, в
следующем формате:

<название продукта>: <название магазина>
Если имеется несколько самых дешевых товаров, то следует вывести тот товар, чье название меньше в лексикографическом
сравнении. Если один товар продается в нескольких магазинах по одной минимальной цене, то следует вывести тот магазин,
чье название меньше в лексикографическом сравнении.

Примечание 1. Разделителем в файле prices.csv является точка с запятой, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. Пример вывода:

Клубничный йогурт: ВкусВилл
Примечание 4. При открытии файла используйте явное указание кодировки UTF-8."""

import csv

with open('prices.csv', encoding='UTF-8') as f:
    h, *rows = csv.reader(f, delimiter=';')
goods = [(r[0], h[x], r[x]) for r in rows for x in range(1, len(h))]
cheapest = min(goods, key=lambda x: (int(x[2]), x[1], x[0]))
print(f'{cheapest[1]}: {cheapest[0]}')
"""Снова не успел
Дан режим работы магазина:

Понедельник	9:00 - 21:00
Вторник	9:00 - 21:00
Среда	9:00 - 21:00
Четверг	9:00 - 21:00
Пятница	9:00 - 21:00
Суббота	10:00 - 18:00
Воскресенье	10:00 - 18:00
Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут, оставшееся до закрытия
магазина.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести количество минут, которое осталось до закрытия магазина, или текст Магазин не работает, если
он закрыт."""

from datetime import date, datetime, timedelta

pattern = '%d.%m.%Y %H:%M'
schedule = {0: (timedelta(hours=9), timedelta(hours=21)),
            1: (timedelta(hours=9), timedelta(hours=21)),
            2: (timedelta(hours=9), timedelta(hours=21)),
            3: (timedelta(hours=9), timedelta(hours=21)),
            4: (timedelta(hours=9), timedelta(hours=21)),
            5: (timedelta(hours=10), timedelta(hours=18)),
            6: (timedelta(hours=10), timedelta(hours=18))
            }
dt = datetime.strptime(input(), pattern)
dt1 = timedelta(hours=dt.hour, minutes=dt.minute)
for k, v in schedule.items():
    if dt.weekday() == k:
        print('Магазин не работает' if dt1 < v[0] or dt1 >= v[1] else int((v[1] - dt1).total_seconds() / 60))
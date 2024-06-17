"""Функция num_of_sundays()
Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:

year — натуральное число, год
Функция должна возвращать количество воскресений в году year.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию num_of_sundays(), но не код,
вызывающий ее."""


from datetime import date


def num_of_sundays(year=int):
    start, end = date(year, 1, 1), date(year, 12, 31)
    return sum(date.fromordinal(i).weekday() == 6 for i in range(start.toordinal(), end.toordinal() + 1))
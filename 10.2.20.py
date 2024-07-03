"""Функция filterfalse()
Реализуйте функцию filterfalse() с использованием функции filter(), которая принимает два аргумента:

predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
iterable — итерируемый объект
Функция должна работать противоположно функции filter(), то есть возвращать итератор, элементами которого являются
элементы итерируемого объекта iterable, для которых функция predicate вернула значение False.

Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве
аргумента значения.

Примечание 2. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном
порядке.

Примечание 3. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию filterfalse(), но не код,
вызывающий ее."""


def filterfalse(predicate, iterable):
    return filter(lambda x: not bool(x), iterable) if predicate is None else filter(lambda x: not predicate(x), iterable)
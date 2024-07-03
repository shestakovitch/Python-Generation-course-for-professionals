"""Функция is_iterable()
Реализуйте функцию is_iterable(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_iterable(), но не код,
вызывающий ее."""


def is_iterable(obj):
    return hasattr(obj, '__iter__')
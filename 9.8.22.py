"""Декоратор takes
Реализуйте декоратор takes, который принимает произвольное количество позиционных аргументов, каждый из которых является
типом данных.

Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, принадлежат одному из этих типов. Если
хотя бы один аргумент не принадлежит одному из данных типов, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также
должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор takes, но не код,
вызывающий его."""

import functools


def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if any(type(i) not in types for i in (*args, *kwargs.values())):
                raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator
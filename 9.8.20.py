"""Декоратор strip_range
Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:

start — неотрицательное целое число
end — неотрицательное целое число
char — одиночный символ, по умолчанию равный точке .
Декоратор должен изменять возвращаемое значение декорируемой функции, заменяя все символы в диапазоне индексов от start
(включительно) до end (не включительно) на символ char.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.

Примечание 2. Гарантируется, что start < end.

Примечание 3. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также
должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимый декоратор strip_range, но не код,
вызывающий его."""

import functools


def strip_range(start: int, end: int, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            value = value[:start] + len(value[start:end])*char + value[end:]
            return value
        return wrapper
    return decorator
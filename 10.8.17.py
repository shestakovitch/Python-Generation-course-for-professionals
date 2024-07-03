"""Функция alnum_sequence()
Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.

Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность натуральных чисел и заглавных
латинских букв:

1,A,2,B,3,C,..,X,25,Y,26,Z

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию alnum_sequence(), но не код,
вызывающий ее."""

from itertools import cycle
from string import ascii_uppercase


def alnum_sequence():
    for item in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
        yield from item
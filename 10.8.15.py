"""Функция tabulate()
Реализуйте функцию tabulate(), которая принимает один аргумент:

func — произвольная функция
Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность возвращаемых значений функции
func сначала с аргументом 1, затем 2, затем 3, и так далее.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию tabulate(), но не код,
вызывающий ее."""

from itertools import count


def tabulate(func):
    yield from (func(i) for i in count(1))
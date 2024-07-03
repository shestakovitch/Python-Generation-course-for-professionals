"""Итератор RandomNumbers
Реализуйте класс RandomNumbers, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:

left — целое число
right — целое число
n — натуральное число
Итератор класса RandomNumbers должен генерировать последовательность из n случайных чисел от left до right включительно,
а затем возбуждать исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс RandomNumbers."""

from random import randrange


class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.n:
            raise StopIteration
        else:
            self.index += 1
            return randrange(self.left, self.right + 1)
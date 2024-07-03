"""Итератор BoundedRepeater
Реализуйте класс BoundedRepeater, порождающий итераторы, конструктор которого принимает два аргумента в следующем
порядке:

obj — произвольный объект
times — натуральное число
Итератор класса BoundedRepeater должен генерировать значение obj times раз, а затем возбуждать исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс BoundedRepeater."""


class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.times == 0:
            raise StopIteration
        else:
            self.times -= 1
            return self.obj
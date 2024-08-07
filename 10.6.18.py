"""Функция all_together()
Реализуйте функцию all_together() с использованием генераторных выражений, которая принимает произвольное количество
позиционных аргументов, каждый из которых является итерируемым объектом.

Функция должна возвращать генератор, порождающий каждый элемент всех переданных итерируемых объектов: сначала все
элементы первого итерируемого объекта, затем второго, и так далее.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию all_together(), но не код,
вызывающий ее."""


def all_together(*args):
    return (i for item in args for i in item)
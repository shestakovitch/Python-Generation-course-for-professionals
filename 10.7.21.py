"""Функция with_previous()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной
элемент итерируемого объекта iterable, а также предшествующий ему элемент:

(<очередной элемент>, <предыдущий элемент>)
Для первого элемента предыдущим считается значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном
порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию with_previous(), но не код,
вызывающий ее."""


def with_previous(iterable, n=None):
    for i in iterable:
        yield i, n
        n = i
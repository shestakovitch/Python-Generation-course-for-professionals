"""Функция primes()
Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:

left — натуральное число
right — натуральное число
Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно, а затем
возбуждающий исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого
себя. Единица простым числом не является.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию primes(), но
не код, вызывающий ее."""


def primes(left, right):
    for cur_num in range(left, right + 1):
        if cur_num == 1:
            continue

        for i in range(2, int(cur_num ** 0.5 + 1)):
            if cur_num % i == 0:
                break
        else:
            yield cur_num
"""Функция get_the_fastest_func()
Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:

funcs — список произвольных функций
arg — произвольный объект
Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление значения при
вызове с аргументом arg наименьшее количество времени.

Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_the_fastest_func(), но не
код, вызывающий ее."""

import time


def calculate_it(func, *args):
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time


def get_the_fastest_func(funcs, arg):
    fastest = None
    for func in funcs:
        if fastest is None:
            fastest = (calculate_it(func, arg), func)
        if fastest > (calculate_it(func, arg), func):
            fastest = (calculate_it(func, arg), func)
    return fastest[1]
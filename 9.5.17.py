"""Функция generator_square_polynom()
Рассмотрим семейство функций — квадратных трехчленов. Все эти функции имеют один и тот же вид:
f(x)=ax**2+bx+c
Реализуйте функцию generator_square_polynom(), которая принимает три аргумента в следующем порядке:
    a — вещественное число, коэффициент a
    b — вещественное число, коэффициент b
    c — вещественное число, коэффициент c
Функция generator_square_polynom() должна возвращать функцию, которая принимает в качестве аргумента вещественное число
x и возвращает значение выражения ax**2+bx+c.

Примечание 1. Рассмотрим пример из первого теста. Вызов generator_square_polynom(1, 2, 1) возвращает функцию,
соответствующую квадратному трехчлену x**2+2x+1.  Функция присваивается переменной f. Далее полученная функция
вызывается с аргументом 5 и возвращает значение 5**2+5⋅2+1=36.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию generator_square_polynom(),
но не код, вызывающий ее."""


def generator_square_polynom(a: int, b: int, c: int):
    def inner(x):
        return a*x**2 + b*x + c
    return inner
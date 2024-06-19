"""Минимум и максимум
Напишите программу, которая определяет минимальное и максимальное значения функции на отрезке в целых точках.

Формат входных данных
На вход программе в первой строке подается корректная функция f(x), в следующей строке вводятся два целых числа a и b,
разделенные пробелом, которые представляют границы отрезка [a;b].

Формат выходных данных
Программа должна определить минимальное и максимальное значения функции f(x) на отрезке [a;b] в целых точках и вывести
полученный результат в следующем формате:

Минимальное значение функции <функция f(x)> на отрезке <отрезок> равно <мин. значение>
Максимальное значение функции <функция f(x)> на отрезке <отрезок> равно <макс. значение>
Примечание 1. Под корректной функцией подразумевается выражение, полностью соответствующее синтаксису языка Python."""

f = input()
a, b = map(int, input().split(' '))
print(f'Минимальное значение функции {f} на отрезке [{a}; {b}] равно {min([eval(f) for x in range(a, b+1)])}\n'
      f'Максимальное значение функции {f} на отрезке [{a}; {b}] равно {max([eval(f) for x in range(a, b+1)])}')
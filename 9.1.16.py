"""Необычная сортировка 🌶️
Дана строка, содержащая латинские буквы и цифры. Напишите программу, которая сортирует символы в строке согласно
следующим правилам:

все отсортированные строчные буквы стоят перед заглавными буквами
все отсортированные заглавные буквы стоят перед цифрами
все отсортированные нечетные цифры стоят перед отсортированными четными
Формат входных данных
На вход программе подается строка, содержащая латинские буквы и цифры.

Формат выходных данных
Программа должна расположить символы в строке в соответствии с условием задачи и вывести полученный результат."""

print(''.join((sorted(input(), key=lambda x: (x.isdigit(), (x.isdigit() and int(x) % 2 == 0), x.isupper(), x.islower(), x)))))
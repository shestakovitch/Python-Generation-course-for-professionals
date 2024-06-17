"""Максимальная группа
Назовем набор различных натуральных чисел группой. Например: (13,4,22,40). Тогда длиной группы будем считать количество
чисел в группе. Например, длина группы (13,4,22,40) равна 4.
Дана последовательность натуральных чисел от 1 до n включительно. Напишите программу, которая группирует все числа
данной последовательности по сумме их цифр и определяет длину группы, содержащей наибольшее количество чисел.
Формат входных данных
На вход программе подается натуральное число n.
Формат выходных данных
Программа должна сгруппировать все числа из натуральной последовательности от 1 до n по сумме их цифр и определить
длину группы, содержащей наибольшее количество чисел.

Примечание 1. Рассмотрим третий тест, в котором n=20. Запишем последовательность чисел от 1 до 20:
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
Сгруппируем полученные числа по сумме их цифр:
(1,10),(2,11,20),(3,12),(4,13),(5,14),(6,15),(7,16),(8,17),(9,18),(19)
Итак, длина группы с наибольшим количеством чисел равна3."""


numbers = list(range(1, int(input()) + 1))
d = {}
for number in numbers:
    d[sum(map(int, str(number)))] = d.get(sum(map(int, str(number))), 0) + 1
print(max(d.values()))
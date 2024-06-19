"""Песочные часы
Напишите программу с использованием рекурсивной функции, которая выводит изображение песочных часов, составленное из
цифр 1, 2, 3, и 4:

1111111111111111    # 16 раз
  222222222222      # 12 раз
    33333333        # 8 раз
      4444          # 4 раза
    33333333        # 8 раз
  222222222222      # 12 раз
1111111111111111    # 16 раз
Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести изображение песочных часов, составленное из цифр 1, 2, 3, и 4, представленное в условии задачи.

Примечание. Количество цифр в каждой строке, указанное в комментариях, выводить не нужно."""


def hourglass(i=1, j=16):
    if i < 4:
        print(f'{str(i) * j:^16}')
        hourglass(i + 1, j - 4)
    print(f'{str(i) * j:^16}')


hourglass()
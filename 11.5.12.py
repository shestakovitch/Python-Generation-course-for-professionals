"""Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют
последовательности символов длины 6, удовлетворяющие следующим условиям:

первый символ — строчная латинская буква
второй символ — цифра, любая буква в произвольном регистре или символ нижнего подчеркивания
третий символ — заглавная латинская буква
четвертый символ должен совпадать с первым символом
пятый символ должен совпадать со вторым символом
шестой символ должен совпадать с третьим символом"""

regex = r'([a-z])(\w)([A-Z])\1\2\3'
"""Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют слова,
записанные дважды подряд. Слова могут быть разделены одним или несколькими пробелами.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами,
соответствующими \W"""

regex = r'\b(\w+)\s+\1\b'
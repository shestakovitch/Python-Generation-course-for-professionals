"""Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют
последовательности из 8 цифр. Причем последовательность может содержать символы дефиса - в качестве разделителей,
только если они делят ее на группы по 2 цифры."""

regex = r'\d{8}|(\d{2}-){3}\d{2}'
"""Каждому гражданину страны Утопия выдается идентификационный номер, который имеет следующий формат:

номер начинается с 0—3 строчных латинских букв включительно
далее следует последовательность цифр, длина которой должна быть от 2 до 8 включительно
после цифр указываются 3 или более заглавные латинские буквы
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют
идентификационные номера граждан Утопии."""

regex = r'[a-z]{,3}\d{2,8}[A-Z]{3,}'
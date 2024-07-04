"""Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют строки,
удовлетворяющие следующим условиям:

строка начинается с одной или двух цифр
после следуют три или более буквы латинского алфавита в произвольном регистре
строка заканчивается тремя или менее точками"""

regex = r'^\d{1,2}[A-Za-z]{3,}\.{0,3}$'
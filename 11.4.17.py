"""Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют строки,
удовлетворяющие следующим условиям:

строка начинается с Mr., Mrs., Ms., Dr. или Er.
оставшаяся часть строки состоит только из одной или более букв латинского алфавита в произвольном регистре"""

regex = r'^[DE]r\.[A-Za-z]+$|^M[rs]\.[A-Za-z]+$|^Mrs\.[A-Za-z]+$'
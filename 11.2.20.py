"""Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют
телефонные номера следующих форматов:

+7xxxxxxxxxx
+7(xxx)xxxxxxx
+7(xxx)-xxx-xx-xx
+7 xxx xxx xx xx
где x — произвольная цифра.

Примечание 1. Дополнительная проверка телефонного номера на корректность не требуется.

Примечание 2. Символы +, ( и ) является метасимволами. Если требуется поиск соответствий самим символам  +, ( и ), то в
регулярном выражении им должен предшествовать символ обратной косой черты  \+, \( и \)."""

regex = r'\+7\d{10}|\+7\(\d{3}\)\d{7}|\+7\(\d{3}\)\-\d{3}\-\d{2}\-\d{2}|\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}'
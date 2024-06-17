'''Функция hide_card()
Реализуйте функцию hide_card(), которая принимает один аргумент:

card_number — строка, представляющая собой корректный номер банковской карты из 
16
16 цифр, между которыми могут присутствовать символы пробела
Функция должна заменять первые 
12
12 цифр в строке card_number на символ * и возвращать полученный результат. Если между цифрами в номере имелись символы пробела, их следует удалить.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию hide_card(), но не код, вызывающий ее.'''


def hide_card(card_number=str):
    return 12 * '*' + card_number.replace(' ', '')[-4:]
"""
Итератор Alphabet 🌶️
Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:

language — код языка: ru — русский, en — английский
Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:

русского алфавита, если language имеет значение ru
английского алфавита, если language имеет значение en
Примечание 1. Буква ё в русском алфавите не учитывается.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Alphabet."""


class Alphabet:
    def __init__(self, language):
        self.language = {'en': [chr(i) for i in range(97, 123)], 'ru': [chr(i) for i in range(1072, 1104)]}[language]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        try:
            return self.language[self.index]
        except IndexError:
            self.index = 0
            return self.language[self.index]
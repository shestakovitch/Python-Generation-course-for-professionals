"""Я в аду?
Напишите программу, которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:

7-ddd-ddd-dd-dd
8-ddd-dddd-dddd
где d — цифра от 0 до 9.

Формат входных данных
На вход программе подается строка произвольного содержания.

Формат выходных данных
Программа должна в введенном тексте найти все телефонные номера, соответствующие форматам, указанным в условии задачи,
и вывести их в том порядке, в котором они были найдены, каждый на отдельной строке."""


def is_phone_number(phone):
    groups = phone.split('-')
    if groups[0] == '7' and len(groups[2]) != 3 or groups[0] == '8' and len(groups[2]) != 4:
        return False
    chars = ''.join(groups)
    return all(c.isdigit() for c in chars)


def get_all_numbers(text):
    for c in range(len(text)):
        chunk = text[c:c + 15]
        if is_phone_number(chunk):
            if chunk.startswith(('7-', '8-', '+7-', '+8-')) and len(chunk) == 15:
                yield chunk


txt = input()
print(*(get_all_numbers(txt)), sep='\n')
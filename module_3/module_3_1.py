# Домашняя работа по уроку "Пространство имён"
# Цель: применить на практике начальные знания о пространстве имён и оператор global. Закрепить навыки из предыдущих модулей.
# Задача "Счётчик вызовов":

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    a = str(string)
    result = (len(a), a.upper(), a.lower())
    count_calls()
    return result


def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:

         return True

    return False


print(string_info('Solovey'))
print(string_info('Wildberis'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN',])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic',])) # No matches
print(calls)

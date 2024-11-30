# 2. Функции, условия, циклы
# Задача 2.1
# Создать функцию calc(a, b, operation)
# 1 Первое число
# 2 Второе число
# Действия над ними:
     # +;-; *, /
     # В остальных случаях возвращать 'Операция не поддерживается'
def calc(a, b, operation):
    result = 'Операция не поддерживается' # Задаем дефолтное значение возвращаемого результата
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b is not int(0):     # проверка деления на 0
            result = a / b
        else:
            result = 'Деление на 0 недопустимо!'
    # Возвращаем результат выполнения функции
    return result
# Проверяем корректные значения

print(calc(30,15,'+'))
print(calc(30,15,'-'))
print(calc(30,15,'*'))
print(calc(30,15,'/'))
# Проверка деления на 0
print(calc(30,0,'/'))
# Проверяем неподдерживаемую операцию
print(calc(30,15,'%'))


# Task 2.2
# Напишите программу, которая будет выводить нечетные числа из списка и остановится, если встретит число 139
def even(num):
    return num % 2 == 0

lst = [1, 34, 78, 345, 111, 8, 5, 34, 9, 3, 139, 56, 2, 67, 69, 90]
# В цикле перебираем элементы выше созданного списка
for i in lst:
    # Если текущий элемент равен 139, то прерываем цикл
    if i == 139:
        break
        # Иначе выводить элементы списка
    else:
        print(i)

# Task 2.3
# Создайте список [18,14,10,6,2] с помощью функции range()
lst_1 = []
# Пробегаемся циклом for по последовательности, которую формирует функция range()
# Начало диапазона : 18
# Конец диапазона: 1 (обратите внимание, что 1 не включается в итоговою последовательность)
# Шаг: -4 (двигаемся в сторону уменьшения значения -0 обратный шаг)
for i in range(18, 1, -4):
    lst_1.append(i)
    print(lst_1)

# Task 2.4
# Дан список lst_2[11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# Необходимо вывести элементы, которые одновременно: 1) меньше 30 и 2) делятся на 3 без остатка.
# Все остальные элементы необходимо просуммировать и вывести конечный результат.

# Задаем константы для значений, заданные в условии
MEDIAN = 30
DIV_NUM = 3
# Создаем список
lst_2 = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# Задаем начальное значение переменной для суммы элементов
sm = 0
# Поочередно перебираем элементы списка
for i in lst_2:
    # Проверяем что:
    # 1) Текущий элемент меньше 30
    # 2) Остаток от деления текущего элемента на 3 равно 0
    if (i < MEDIAN) and (i % DIV_NUM == 0):
        print(i)
        # Добавляем элемент к сумме, если условие не выполнено
    else:
        sm += i
        # Выводим конечную сумму
print('Sum:', sm)

# Task 2.5
# Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона,
# к которому относится этот месяц.
# Например, передаем 2, на выходе получаем 'Зима'.
# Имя функции: month_to_season
# Параметр: month
def month_to_season(month):
    # Создание словаря для хранения информации о сезонах
    # Ключ: кортеж(tuple) из номеров входящих в сезон месяцев
    # Значение: строка(str)-название сезона
    season_ranges = {
        (12, 1, 2): 'Winter',
        (3, 4, 5): 'Spring',
        (6, 7, 8): 'Summer',
        (9, 10, 11): 'Autumn'
    }
    # Создание переменной для возвращаемого значения функции
    season = None

    # Цикл, в котором по очереди перебираются пары ключ-значение(номера месяцев - сезон) из словаря
    for key, value in season_ranges.items():
        # Если значение входного параметра(номер месяца) входит в состав ключа(пример ключа - (3, 4, 5))
        if month in key:
            # То присваиваем возвращаемой переменной season название сезона
            season = value
            # Останавливаем цикл
            break

    # Возвращаем название сезона
    return season

# Проверяем работу функции
print(month_to_season(1))
print(month_to_season(5))
print(month_to_season(8))
print(month_to_season(9))
print(month_to_season(12))
print(month_to_season(999))
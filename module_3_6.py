# Встроенные функции в Python
# int()  --> int(input())
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()
salary = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
print(round(sum(salary)/len(salary), 2), ' - средняя зарплата в компании')
print(round(max(salary), 2), ' - максимальная зарплата в компании')
print(round(min(salary), 2), ' - минимальная зарплата в компании')

names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = dict(zip(names, salary))
print(zipped['Денис'], '- зарплата Дениса')


# Встроенные функции 1.2
a = [1, 1, 1]
b = ''
d = [1, 1, 1]
c = d
c[0] = 2
print(c)
print(d)
print(id(a))
print(id(d))
print(id(c))
print(c is d)


def helper():
    """
    Эта функция-помощник
    """
    pass

print(helper.__doc__)


# Практика по функциям
# Максимум в списке
# Подсчёт четных чисел в списке
# Уникальный список


def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_


# print(find_max([1, 2, 1, 5, 0]))


def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter


# print(count_even([2, 2, 3, 4, 2, 1, 0]))

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list


print(unique([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]))

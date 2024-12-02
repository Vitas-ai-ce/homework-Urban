# Домашнее задание по уроку "Распаковка позиционных параметров".

# Задача "Распаковка":

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print()
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [6, 5, 7], 'hello', 1>0
values_dict = {'a' : 25, 'b' : 6, 'c' : 87}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = 3.14, 'Пи'
print_params(*values_list_2, 42)
# def append_to_list(item, list_my=None):
#   if list_my is None:
#    list_my = []
#   list_my.append(item)
#   list_my
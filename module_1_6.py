# Работа со словарями!
my_dict = {'Vitaliy': 1987, 'Elena': 1990, 'Vladimir': 2008}
print(my_dict)
print(my_dict['Elena'])
print(my_dict.get('Sonya'))
my_dict.update({'Evgeniy': 2020,
                'Sofia': 2022})
print(my_dict)
a = my_dict.pop('Vitaliy')
print(a)
print(my_dict)

# Работа с множествами
my_set = { 1, 2, 6, 'phone', True, (9, 8, 7)}
print(my_set)
my_set.add(75.5)
my_set.remove(6)
print(my_set)


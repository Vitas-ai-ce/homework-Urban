# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else"
from time import sleep
first = int(input('Введите целое число:'))
second = int(input('Введите целое число:'))
third = int(input('Введите целое число:'))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    sleep(3)
    print(0)
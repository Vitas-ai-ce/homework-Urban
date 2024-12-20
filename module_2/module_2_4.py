# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # исходный список
n = 0 # Проверяемое число
primes = []  # Простое число — это натуральное число больше 1,
# у которого есть всего два делителя: единица и само число.
not_primes = []  #  Это точно такое же натуральное число больше единицы,
# которое делится на единицу, на само себя и еще хотя бы на одно натуральное число.
i = 0
for i in range(len(numbers)):
    is_prime = True  # признак простого числа
    n = numbers[i]
    if n < 2:
        continue
    else:
        k = n ** (1 / 2)  # Корень квадратный из n
    for a in range(2, int(k + 1)):
        if n % a == 0:
            is_prime = False
            break

    if not is_prime:
        not_primes.append(n)
    else:
        primes.append(n)
is_prime = True  # признак простого числа
print('primes',primes)
print('not_primes',not_primes)
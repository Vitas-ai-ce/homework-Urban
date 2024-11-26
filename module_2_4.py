numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i > 1:
        i += 1
        is_prime = True
        for is_prime in range(2, i, len(numbers)):
            if (i % is_prime) == 0:
                is_prime += 1
                not_primes.append(i)
                break
            else:
                 primes.append(i)

            print('primes',primes)
            print('not_primes',not_primes)
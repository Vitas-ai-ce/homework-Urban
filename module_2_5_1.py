# Дополнительное практическое задание по модулю: "Основные операторы"

# "Слишком древний шифр":

import random

def get_cipher():  # получим число первого поля
    numbers = list(range(3, 21))
    cipher = random.choice(numbers)
    return cipher

def get_passcode ():
    codepassword = {}  # создаём словарь с кодами и паролями
    codepassword.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    codepassword.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    codepassword.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    codepassword.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    codepassword.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    codepassword.update({20: 13141911923282183731746416515614713812911})
    passcode = codepassword.get(n)
    return passcode

n = get_cipher()
# n = int(input('введите шиифр :'))
print('Шифр   :', n)
# print('Пароль :', get_passcode(n))

pairing_num1 = list(range(1, n))
pairing_num2 = list(range(1, n))
pairs = []
result = ''

for i in pairing_num1:
    for j in pairing_num2:
        pn1 = i  #  pairing_num1[i]
        pn2 = j  # pairing_num2[j]
        if pn1 >= pn2:
            continue
        else:
            multiple = n % (pn1 + pn2)
            if multiple == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print('Пары чисел', *pairs)
print('Введите пароль', result, 'во второе поле')
if int(result) == get_passcode():
    print('Ворота открываются!')

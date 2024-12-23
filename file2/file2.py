# программа для тренировки скорости письма
# Minimal Valuable Product
'''
- генерация текста V
- работа с пользователем V
- обработка полученного текста V
- вывод результатов
- работа с таблицей рекордов
'''

def gen_text(n = 5):
    import names
    l = []
    for i in range(n):
        l.append(names.get_full_name())
    return ', '.join(l)

def user_input(text):
    import time
    print('Приготовьтесь вводить текст')
    time.sleep(1)
    for i in range(3,0,-1):
        print(i)
        time.sleep(0)

    start = time.time()
    user_text = input(text)
    stop = time.time()
    user_time = stop - start
    return user_text, int(user_time)


def similarity(s1, s2):
    import difflib
    matcher = difflib.SequenceMatcher(None, s1, s2)
    return matcher.ratio()

def output(user_text,sim,user_time):
    import pandas as pd
    from datetime import datetime
    print(f'Вы напечатали {len(user_text)} символов за {user_time} секунд')
    print(f'Ваша точность составила {int(sim*100)} % и итог: {int(len(user_text)/user_time*60*sim)} символов в минуту')
    # имя длина время точность дата
    df = pd.read_csv('table.csv')
    df.loc[len(df)] = [input('Введите ваше имя: '), len(user_text), user_time, int(sim*100), datetime.today()]
    print(df)
    df.to_csv('table.csv', index = False)


text = gen_text()
user_text, user_time = user_input(text+'\n: ')
sim = similarity(text, user_text)
output(user_text,sim,user_time)
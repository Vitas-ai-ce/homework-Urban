# Самостоятельная работа по уроку "Произвольное число параметров"
# Ваша задача:
# Цель: закрепить знание использования параметров *args/ **kwargs на практике.
# Задача "Однокоренные":

def single_root_words(root_word, *other_words ):
    same_words = [] # список однокоренных слов
    for word in other_words: # перебрать слова в other_words
        if str(root_word).startswith(word) or word.startswith(root_word): # если строка root_word начинается с(слова)
            # или слово начинается с корневого слова (root_word)
            if word.upper() or word.lower() in other_words: # если слова в верхнем регистре
                # или слова в нижнем регистре в other_words
                same_words.append(word) # добавить в список те же слова(same_words)
    return same_words # вернуть те же_слова (same_words)

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))



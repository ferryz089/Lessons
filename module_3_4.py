def single_root_words(root_word, *other_words): # Создаем функцию
    same_words = []                             # Создаем пустой список
    for i in other_words:                       # Создаем цикл, перебирающий каждый элемент кортежа other_words
        if root_word.lower() in i.lower() or i.lower() in root_word.lower(): # условие вхождения root_word и наоборот
            same_words += [i]                   # Добавляем необходимый элемент кортежа в список
        else:
            continue                            # Продолжаем цикл до конца
    return same_words                           # Возвращаем готовый список из функции

# Примеры из домашнего задания:
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print('Список однокоренных слов с "rich": ',result1)        # Выводим печать
print('Список однокоренных слов с "Disablement": ',result2) # Выводим печать
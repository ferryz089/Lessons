from math import inf                    # Импортируем бесконечность из библиотеки math
def divide(first, second):              # Создаем функцию второго модуля
    if second == 0:                     # условие1
        return inf                      # возвращаем бесконечность
    if second != 0:                     # условие2
        return first/second             # возвращаем результат деления
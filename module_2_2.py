first = int(input('Введите целое первое число: ')) # вводим числа в переменные
second  = int(input('Введите целое второе число: '))
third  = int(input('Введите целое третье число: '))
if first == second == third:                        # формируем сначала самое сложное условие
    print('Число совпадений: ', 3)                  # печать числа свопадений
elif first == second != third or first != second == third or first == third != second: # формируем среднее условие
    print('Число совпадений: ', 2)                  # печать числа свопадений
else:                                               # формируем остаточное условие
    print('Число совпадений: ', 0)                  # печать числа свопадений
def get_multiplied_digits(number):                       # Создаем функцию
    str_number = str(number)                             # Создаем переменную строку из параметра функции
    first = int(str_number[:1])                          # Создаем переменную из первого числа параметра
    if len(str_number) == 1 and number > 0:              # Условие остановки рекурсии_1
        return first
    if int(str_number[1:]) == 0 and len(str_number) > 1: # Условие остановки рекурсии_2
        return first
    if len(str_number) > 1:                              # Условие рекурсии
        return first * get_multiplied_digits(int(str_number[1:]))


# Пример из домашнего задания:
result = get_multiplied_digits(40203)
print('Результат домашнего примера: ',result)
# Проверим добавив ввод любого числа с клавиатуры :
nums_ = int(input('Введите число: '))
result = get_multiplied_digits(nums_)
print('Результат рекурсии: ', result)                    # Выводим печать из функции
# Создадим начальную переменную подсчета результата и цикл чтобы проверить правильность расчета рекурсии:
res_ = 1
for i in list(str(nums_)):
    if int(i) > 0:
        res_ = res_ * int(i)
print('Результат цикла: ', res_)                         # Выводим печать из цикла

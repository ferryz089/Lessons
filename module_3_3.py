def print_params(a = 1, b = 'строка', c = True): # Создаем функцию
    print(a, b, c)

# Выводим пункты задания с необходимыми переменными
# 1.Функция с параметрами по умолчанию:
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
# 2.Распаковка параметров:
values_list = [5, 'Отчет', True]
values_dict = {'a' : [1, 2, 3], 'b' : False, 'c' : 18}
print(f'Распаковка списка: ')
print_params(*values_list)
print('Распаковка словаря: ')
print_params(**values_dict)
# 3.Распаковка + отдельные параметры:
values_list_2 = [[57, 'Age'], True]
print('Распаковка + отдельный параметр: ')
print_params(*values_list_2, 42)
my_dict = {str(input('введите свое имя ')): int(input('введите год рождения ')),
           str(input('введите имя почтового ящика через @ ')): str(input('введите пароль от ящика ')),
           'номер телефона': int(input('введите номер телефона'))}

print('Информация о пользователе_v1:', my_dict)
print('номер телефона', my_dict.get('номер телефона'))
print('почтовый индекс', my_dict.get('почтовый индекс', 'не вводился'))
my_dict.update({'почтовый индекс': int(input('введите почтовый индекс ')),
               'город': str(input('введите ваш город '))})
print('Информация о пользователе_v2:', my_dict)
print('Удаленный ключ', my_dict.pop('почтовый индекс'))
print('Информация о пользователе_v3:', my_dict)

my_set = {int(input('1) введите любое число ')), int(input('2) повторите число ')),
          str(input('3) введите любой текст ')), str(input('4) повторите текст ')),
          (int(input('5) введите любое число ')), int(input('6) введите любое число ')), str(input('7) введите любой текст '))),
          2 + 2 == int(input('4) 2 + 2 = введите ответ '))}
print('Множество_v1 :', my_set)
my_set.update({str(input('введите любой текст ')), int(input('введите любое число '))})
my_set.discard(True)
print('Множество_v2 :', my_set)


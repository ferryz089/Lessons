import random                                 #Импортируем библиотеку случайных чисел
number = random.randrange(3, 20)              #Создаем переменную с перебором случайных чисел от 3 до 20
print('Число в первом поле: ', number)        #Выводим на печать
result = ""                                   #Создаем переменную с пустой строкой для цикла
#number = 20                                  #Для примера  переменная number, равная 20

for n in range(1, 20):                        #Создаем цикл с вложенным в него, во внешнем перебираем первую цифру пары
    for i in range(n + 1, 20):                #Во внутреннем перебираем вторую цифру пары
        if number % (i + n) == 0:             #Условие кратности первого числа сумме пары чисел
            result += f'{n}{i}'               #Расширяем список с помощью f-строки в диапазоне цикла

print('Пароль: ', result)                     #Выводим на печать

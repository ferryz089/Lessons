import random                                 #Импортируем библиотеку случайных чисел
number = random.randrange(3, 20)   #Создаем переменную с перебором случайных чисел от 3 до 20
print('Число в первом поле: ', number)        #Выводим на печать
result = ""                                   #Создаем переменную с пустой строкой для цикла
#number = 20                                  #Для примера  переменная number, равная 20

for n in range(1, 20):                        #Создаем цикл с вложенным в него, во внешнем перебираем первую цифру пары
    for i in range(n + 1, 20):                #Во внутреннем перебираем вторую цифру пары
        if number % (i + n) == 0:             #Условие кратнойсти первого числа суммы пары чисел
            result += f'{n}{i}'               #Расширяем список с помощью f-строки в диапазоне цикла
            #result += [[n, i]]
            #result = sorted(result)
print('Пароль: ', result)                     #Выводим на печать
#print(*result)
'''''
def secondary_number():
    global result
    #print(*result)
    s_ = []
    for k in range(len(result))[1::2]:
        for m in range(len(result))[::2]:
            if k - m == 1 and len((result)) % 2 == 0:
                s_ += [int(f'{result[m]}{result[k]}')]
            if k - m == 1 and len((result)) % 2 != 0:
                s_ += [int(f'{result[m]}{result[k]}')]
            if m == len(result) - 3 and k - m == 1 and len((result)) % 2 != 0:
                s_ += [int(f'{result[len(result) - 1]}')]
                break
                s_ = s_[len(s_)/2::]
    result = s_
    #print(*s_)

    return s_
secondary_number()
secondary_number()
secondary_number()
secondary_number()
print(*result)
            #    results = print(result[j])
        #else:
        #    continue
        #if number % (number - n) == 0 and n < number - n:
            #print(n, number - n)
        #if n >= number - n:
        #    continue
        #print(n, number - n)

#result = sorted(result)
#results = sum(results)
#print(result)


''
s_ = []
print(result)
for j in range(len(result)):
    s_ += [int(f'{result[j][0]}{result[j][1]}')]
t_ = []
for k in range(len(s_))[1::2]:
    for m in range(len(s_))[::2]:
        if k - m == 1 and len((s_)) %2 == 0:
            t_ += [int(f'{s_[m]}{s_[k]}')]
        if k - m == 1 and len((s_)) %2 != 0:
            t_ += [int(f'{s_[m]}{s_[k]}')]
        if m == len(s_) - 3 and k - m == 1 and len((s_)) %2 != 0:
            t_ += [int(f'{s_[len(s_) - 1]}')]
            break
v_ = []
for k in range(len(t_))[1::2]:
    for m in range(len(t_))[::2]:
        if k - m == 1 and len((t_)) %2 == 0:
            v_ += [int(f'{t_[m]}{t_[k]}')]
        if k - m == 1 and len((t_)) %2 != 0:
            v_ += [int(f'{t_[m]}{t_[k]}')]
        if m == len(t_) - 3 and k - m == 1 and len((t_)) %2 != 0:
            v_ += [int(f'{t_[len(t_) - 1]}')]
            break
w_ = []
for k in range(len(v_))[1::2]:
    for m in range(len(v_))[::2]:
        if k - m == 1 and len((v_)) %2 == 0:
            w_ += [int(f'{v_[m]}{v_[k]}')]
        if k - m == 1 and len((v_)) %2 != 0:
            w_ += [int(f'{v_[m]}{v_[k]}')]
        if m == len(v_) - 3 and k - m == 1 and len((v_)) %2 != 0:
            w_ += [int(f'{v_[len(v_) - 1]}')]
            break
z_ = []
for k in range(len(w_))[1::2]:
    for m in range(len(w_))[::2]:
        if k - m == 1 and len((w_)) %2 == 0:
            z_ += [int(f'{w_[m]}{w_[k]}')]
        if k - m == 1 and len((w_)) %2 != 0:
            z_ += [int(f'{w_[m]}{w_[k]}')]
        if m == len(w_) - 3 and k - m == 1 and len((w_)) %2 != 0:
            z_ += [int(f'{w_[len(w_) - 1]}')]
            break

print(*s_)
print(*t_)
print(*v_)
print(*w_)
print(*z_)
13141911923282183731746416515614713812911
13141923283746119218317416515614713812911
13141911923282183731746416515614713812911
13141911923282183731746416515614713812911
13141911923282183731746416515614713812911'''



















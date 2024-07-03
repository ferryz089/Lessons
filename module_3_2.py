def send_email(message, recipient, sender="university.help@gmail.com"): # Создаем функцию
    not_right_email = f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}' #локальная переменная принта
    if "@" not in recipient or "@" not in sender: # условие отсутствия @
        print(not_right_email)                    # выводим локальную переменную
        return                                    # возвращаем функцию
    elif ".com" not in sender and ".ru" not in sender and ".net" not in sender: # условие отсутствия доменов отправителя
        print(not_right_email)                    # выводим локальную переменную
        return                                    # возвращаем функцию
    elif ".com" not in recipient and ".ru" not in recipient and ".net" not in recipient: # усл. отсутствия у получателя
        print(not_right_email)                    # выводим локальную переменную
        return                                    # возвращаем функцию
    if sender == recipient:                       # условие равенства ящиков отправителя и получателя
        print('Нельзя отправить письмо самому себе!') # выводим комментарий
        return                                    # возвращаем функцию
    if sender == "university.help@gmail.com":     # условие равенства ящика отправителя стандартному
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}') # выводим комментарий
        return                                    # возвращаем функцию
    else:                                         # прочие условия
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}') # выводим коммент
        return                                    # возвращаем функцию


# ниже вводим обращения к функции с параметрами из задания, кроме последнего
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
print()
send_email('Это сообщение для проверки связи', 'vasyok1337gmail.com') # пример отсутствия @
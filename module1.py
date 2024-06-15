balls_1 = list(input('Введите оценки ученика №1 последовательно: ')) #Вводим оценки первого по списку ученика
balls_1 = [int(balls_1[i]) for i in range(len(balls_1))] #Преобразуем полученный выше список в список с целыми числами
balls_2 = list(input('Введите оценки ученика №2 последовательно: ')) #Повторяем то, что выше еще для четырех учеников:
balls_2 = [int(balls_2[i]) for i in range(len(balls_2))]
balls_3 = list(input('Введите оценки ученика №3 последовательно: '))
balls_3 = [int(balls_3[i]) for i in range(len(balls_3))]
balls_4 = list(input('Введите оценки ученика №4 последовательно: '))
balls_4 = [int(balls_4[i]) for i in range(len(balls_4))]
balls_5 = list(input('Введите оценки ученика №5 последовательно: '))
balls_5 = [int(balls_5[i]) for i in range(len(balls_5))]
grades = [balls_1, balls_2, balls_3, balls_4, balls_5] #создаем список из списков оценок
print('Список из оценок: ', grades)
#grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] строка из задания

sum_ball = [sum(grades[i])/len(grades[i]) for i in range(len(grades))] #создаем список из средних оценок каждого ученика
print('Список из средних значений оценок: ', sum_ball)

name_stud_1 = str(input('Введите имя ученика №1: ')) #Вводим имена кадого из учеников
name_stud_2 = str(input('Введите имя ученика №2: '))
name_stud_3 = str(input('Введите имя ученика №3: '))
name_stud_4 = str(input('Введите имя ученика №4: '))
name_stud_5 = str(input('Введите имя ученика №5: '))
students = {name_stud_1, name_stud_2, name_stud_3, name_stud_4, name_stud_5} #создаем множество из имен учеников
#students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} строка из задания
students = sorted(list(students)) #применяем сортировку в алфавитном порядке
print('Имена студентов в алфавитном порядке', students)

ball_students = dict(zip(students, sum_ball)) #упаковываем списки выше в словарь, где каждому имени в алфавитном порядке присваивается средний балл по оценкам
print('Средний балл каждого ученика: ', ball_students)

print("Количество выполненных ДЗ")
num_hom_works = int(input("запишите значение 12"))

print("Количество затраченных часов")
num_hours = float(input("запишите значение 1.5"))

print("Название курса")
name_curse = input("запишите значение Python")

print("Время на одно задание")
time_one_hw = num_hours / num_hom_works
print(time_one_hw)

print(name_curse + ", всего задач:", num_hom_works, ", затрачено часов:", num_hours, ", среднее время выполнения ", time_one_hw, "часа.")
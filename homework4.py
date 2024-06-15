#
my_string = input("введите название региона: ")
print("длина символов введённого текста: ", len(my_string))
print("строка в верхнем регистре: ", my_string.upper())
print("строка в нижнем регистре: ", my_string.lower())
print("строка без пробелов: ", my_string.replace(" ", ''))
print("первый символ строки: ", my_string[0:1])
print("последний символ строки: ", my_string[-1:-2:-1])

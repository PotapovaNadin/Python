# задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет
# - 

# try:
#     day = int(input("Введите число дня недели: "))
#     if day > 5 and day < 8:
#         print('Указанный день является выходным')
#     elif day < 6:
#         print('Указанный день не является выходным')
#     else:
#         print('Введите число от 1 до 7')
# except:
#     print('Введите число от 1 до 7')

# задача 2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# try:
#     x = int(input('Введите значение x: '))
#     y = int(input('Введите значение y: '))
#     z = int(input('Введите значение z: '))

#     a = not(x or y or z)
#     b = not x and not y and not z

#     if a == b:
#         print(True)
#     else:
#         print(False)
# except:
#     print('Введите целое число')


# задача 3. Напишите программу, которая принимает на вход 
# координаты точки (X и Y), и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# try:

#     x = int(input('Введите значение x: '))
#     y = int(input('Введите значение y: '))

#     if x > 0 and y > 0:
#         print('1 четверть')
#     elif x > 0 and y < 0:
#         print('2 четверть')
#     elif x < 0 and y < 0:
#         print('3 четверть')
#     elif x < 0 and y > 0:
#         print('4 четверть')
#     elif x == 0:
#         print('x находится на оси y')
#     elif y == 0:
#         print('y находится на оси x')
# except:
#     print('Введите число')

# задача 4 HARD необязательная Напишите простой калькулятор, 
# который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, 
# после чего применяет операцию к введённым числам 
# ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, 
# где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, 
# необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!
# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0
# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

try:
    num1 = float(input('Введите первое число '))
    oper = str(input('Введите операцию '))
    num2 = float(input('Введите второе число '))

    if oper == '+':
        print(num1 + num2)
    elif oper == '-':
        print(num1 - num2)
    elif oper == '/':
        if num2 == 0:
            print('Деление на 0!')
        else:
            print(num1 / num2)
    elif oper == '*':
        print(num1 * num2)
    elif oper == 'mod':
        if num2 == 0:
            print('Деление на 0!')
        else:
            print(num1 % num2)
    elif oper == 'pow':
        print(num1 ** num2)
    elif oper == 'div':
        if num2 == 0:
            print('Деление на 0!')
        else:
            print(num1 // num2)
except:
    print(' Введите число ')
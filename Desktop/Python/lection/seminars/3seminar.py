# def summa_numbers(): #эта функця ничего не возвращает, только печатает на экран
# a=3
# b=6
# print(a+b)

# #summa1()

# def summa2(): #эта функця уже возвращает значение
# a=int(input("Введите первое число "))
# b=int(input("Введите второе число "))
# return a+b

# #print(summa2())

# x1=6
# x2=5

# def summa3(): #эта функця уже возвращает значение на основе глобальных переменных - не профессионально
# return x1 + x2

# #print(summa3())
# sum = 0

# def summa4(): #эта функця изменяет глобальную переменную
# global sum
# a=int(input("Введите первое число "))
# b=int(input("Введите второе число "))
# sum = a + b

# #summa4()
# #print(sum)

# def summa5(a,b): #эта функция уже принимает на вход аргументы и возвращает значение
# return a+b

# try:
# a1=int(input("Введите первое число "))
# b1=int(input("Введите второе число "))
# print(summa5(a1, b1))
# except:
# print("надо было вводить именно целое число")


# ПРОВЕРКА ЧИСЛА!!

# def check_digit(text):
# check = False
# while not check:
# try:
# number = int(input(f"{text}"))
# check = True
# except ValueError as error:
# print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
# return number

# 3. Задайте список из n чисел последовательности (1+1/N)**N 
# и выведите на экран их сумму.

# n = int(input('Введите целое число: '))
# list = []

# def find_sum(n):
#     sum = 0
#     for i in range(n):
#         list_number = (1+1/n)**n
#         list.append(list_number)
#         sum += list_number
#     return list, sum

# sum_of_numbers = find_sum(n)
# print(f'Сумма чисел последовательности равна {sum_of_numbers}')


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# m = int(input('Введите число: '))
# list1 = []
# for i in range(-m,m):
#     list1.append(i)
# print(list1)

# path = 'file1.txt'
# data = open(path, 'r')
# prod = 1
# for line in data:
#     prod *= list1[int(line)]
# print(prod)
# data.close()

# 20. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# def create_string_list(number):
#     list = []
#     for i in range(number):
#         list.append(input('Введите что-нибудь: '))
#     return list

# def check_value_in_list(list, number):
#     for i in list:
#         if i == number:
#             print('В списке присутствует ваше число!')

# try:
#     num = input('Введите искомое число: ')
#     size = int(input('Введите размер списка: '))
#     list = create_string_list(size)
#     check_value_in_list(list, num)

# except:
#     print('Некорректный ввод!')


# 21. Напишите программу, которая определит позицию второго вхождения строки 
# в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# def create_string_list(number):
#     list = []
#     for i in range(number):
#         list.append(input('Введите что-нибудь: '))
#     return list

# def check_double_first_value(list, find):
#     check = 0
#     find_index = -1
#     for i in range(len(list)):
#         if list[i] == find:
#             check += 1
#         if check == 2:
#             find_index = i
#             break
#     return find_index

# size = int(input('Введите размер списка: '))
# list = create_string_list(size)
# find = input('Ищем: ')
# if check_double_first_value(list, find) == (-1):
#     print('Нет повторов')
# else:
#     print(f'Искомый элемент стоит на {check_double_first_value(list,find)} позиции.')

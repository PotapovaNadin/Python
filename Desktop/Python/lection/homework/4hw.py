# задача 1. 
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# try:
#     n = int(input("Введите число: "))

#     def find_multipliers(n):
#         list = []
#         i = 2
#         while i <= n:
#             if n % i == 0:
#                 list.append(i)
#                 n //= i
#                 i = 2
#             else:
#                 i += 1
#         return(list)
#     multipliers = find_multipliers(n)
#     print(multipliers)
# except:
#     print('Введите целое число')

# задача 2 . 
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# import random
# try:
#     n = int(input('Введите размер списка: '))
# except:
#     print('Введите целое число!')
# list = []
# def create_list(n):
#     i = 0
#     while i < n:
#         list_number = random.randrange(1, 10)
#         list.append(list_number)
#         i +=1
#     return(list)

# list_of_numbers = create_list(n)
# print(f'Сформировали список рандомных чисел {list_of_numbers}')

# def only_one_numbers(list):
#     new_list = []
#     for i in list:
#         if i not in new_list:
#             list_number = i
#             new_list.append(list_number)
#     return(new_list)

# list1 = only_one_numbers(list)
# print(f'Список неповторяющихся элементов {list1}')

# задача 3. 
# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# def write_file(st):
#     with open('file4.txt', 'w') as data:
#         data.write(st)


# def rnd():
#     return random.randint(0,101)


# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))

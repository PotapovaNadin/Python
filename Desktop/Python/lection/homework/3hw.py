# Задача 1 Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# *Пример:*
# - [2, 3, 5, 9, 3] 
# -> на нечётных позициях элементы 3 и 9, ответ: 12

try:
    n = int(input('Введите размер списка: '))
except:
    print('Введите целое число!')
list = []
def create_list(n):
    for i in range(n):
        try:
            list_number = int(input(f'Введите число {i+1} '))
            list.append(list_number)
        except:
            print('Введите целое число!')
    return(list)

list_of_numbers = create_list(n)
print(list_of_numbers)

def sum_num(n, list):
    sum = 0
    for i in range(n):
        if i % 2 != 0:
            print(f'На нечетной позиции в списке находится элемент {list[i]}')
            sum += list[i]
    return(sum)

sum_of_negative = sum_num(n, list)
print(f'Сумма элементов на нечетных позициях равна {sum_of_negative}')


# Задача 2. Напишите программу, 
# которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# try:
#     n = int(input('Введите количество элементов в списке : '))
# except:
#     print('Введите челое число!')

# a = []
# def create_list(n):
#     for i in range(n):
#         try:
#             a_number = int(input(f'Введите число {i+1} '))
#             a.append(a_number)
#         except:
#             print('Введите целое число!')
#     return(a)

# list_of_numbers = create_list(n)
# print(list_of_numbers)

# new1 = []
# new2 = []
# def create_new_lists(n, new1, new2):
#     for i in range(int(n/2)):
#         new_number = a[i]
#         new1.append(new_number)
#     if n % 2 != 0:
#         new_number = a[int(n/2)]**2
#         new1.append(new_number)
#     for i in range(1, int (n/2)+1):
#         new_number = a[i*(-1)]
#         new2.append(new_number) 
#     return(new1, new2)

# new_lists = (create_new_lists(n, new1, new2))
# print(new_lists)

# def list_result(new1, new2):
#     for i in range(len(new2)):
#         new1[i]= new1[i]*new2[i]
#     return(new1)

# result_lst = list_result(new1, new2)
# print(result_lst)


# Задача 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# try:
#     n = int(input('Введите количество элементов в списке : '))
# except:
#     print('Введите целое число!')
# a = []
# def create_list(n):
#     for i in range(n):
#         try:
#             a_number = float(input(f'Введите число {i+1} '))
#             a.append(a_number)
#         except:
#             print('Введите вещественное(дробное) число!')
#     return(a)
# list = create_list(n)
# print(list)

# def find_max(a, n):
#     max = a[0]
#     for i in range(n):
#         if a[i] > max:
#             max = a[i]
#     return(max)
# max_a = find_max(a, n)
# print(f'Максимальное число списка: {max_a}')

# def find_min(a, n):
#     min = a[0]
#     for i in range(n):
#         if a[i] < min:
#             min = a[i]
#     return(min)
# min_a = find_min(a, n)
# print(f'Минимальное число списка: {min_a}')

# result = max_a - min_a
# print(f'Разница между максимальным и минимальным числами списка равна: {result}')

# Задача 4. Напишите программу, 
# которая будет преобразовывать десятичное число в двоичное. 
# Нельзя использовать готовые функции.

# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# list = [] 
# new_list = []
# try:
#     n = int(input('Введите целое число: '))
# except:
#     print('Введите целое число!')
# def convert_dec(n):
#     while n > 0:
#         list_number = n%2
#         list.append(list_number)
#         n = (n // 2)
#     for i in range(1, len(list)+1):
#         list_num = list[i*(-1)]
#         new_list.append(list_num)
#     return(new_list)

# dec = convert_dec(n)
# print(f'Двоичное число {n} в десятичной системе будет выглядеть как {dec}')

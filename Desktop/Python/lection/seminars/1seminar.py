# Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.

# первый вариант

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))

# if num1 == num2*num2 or num2 == num1*num1:
#     print(f'одно число является квадратом другого')
# else:
#     print(f'ни одно из чисел не является квадратом другого')

# второй вариант

# try:
#     number1 = int(input('Введите первое число: '))
#     number2 = int(input('Введите второе число: '))
#     if number1 ** 2 == number2:
#         print(f'{number2} является квадратом числа {number1}')
#     elif number2 ** 2 == number1:
#         print(f'{number1} является квадратом числа {number2}')
#     else:
#         print('Ни одно из чисел не является квадратом другого')
# except:
#     print('Введите целое число ')


# 2. Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.

# вариант 1

# def create_list():
#     array = []
#     for i in 5:
#         value = int (input("Введите число: "))
#         array.append(value)
#     return array

# def find_max(array):
#     max = array[0]
#     for i in range(len(array)):
#         if array[i] > max:
#             max = array[i]
#     return max

# res = create_list()
# print(res)
# max =find_max(res)
# print(f'Максимальное значение в списке равно {max}')

# вариант 2

# try:
#     numbers = []
#     for i in range(5):
#         numbers.append(int(input(f'Введите число {i+1}: ')))
#         max_num = numbers[0]
#         min_num = numbers[0]
#         index_max = 0
#         index_min = 0
#         sum = 0
#     for i in range(len(numbers)):
#         sum += numbers[i]
#     if numbers[i] > max_num:
#         max_num = numbers[i]
#         index_max = i
#     elif numbers[i] < min_num:
#         min_num = numbers[i]
#         index_min = i
#     print('Максимальное число =', max_num, 'Индекс = ', index_max)
#     print('Минимальное число =', min_num, 'Индекс = ', index_min)
#     print('Среднее арифметическое = ', sum/len(numbers))
# except:
#     print('Введите целое число')

# 1. Напишите программу, которая будет на вход принимать число N
# и выводить числа от -N до N.

# *Примеры:* 

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5\

# вариант 1

# try:
#     n = int(input('Введите число n: '))
#     r = range(-n, n+1)
#     for i in r:
#         print (i)

# except:
#     print('Введите целое число')

# вариант 2

# try:
#     n = int(input('enter n:'))

#     for i in range(-n, n + 1):
#         print(i, end = ', ')

# except:
#     print('enter numbers')

# вариант 3

# try:
#     list = []
#     n = int(input("Введите число N: "))
#     for i in range(-n,n+1):
#         list.append(i)
#     print(list)

# except:
#     print("Введите целое число")

# 2. Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# вариант 1

# x = (input('enter x: '))
# if int(x) - x == 0:
#     print('no')
# else:
#     print(int(x * 10 % 10))

# 3. Напишите программу, которая принимает на вход число 
# и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# def multiple(num):
#     if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
#         print("Число удовлетворяет данным условиям")
#     else:
#         print("Число не удовлетворяет данным условиям")
# try:
#     num = int(input("Введите число: "))
#     multiple(num)
# except:
#     print('Введите целое число')
# 13.09.24 cw 1 and 2 tasks

# print('Ваши фамилия, имя?')
# name = input()
# print('Сколько вам лет?')
# age = input()
# print('Где вы живете?')
# placeofliving = input()

# print(f'\n Ваше фамилия, имя {name} \n Ваш возраст {age} \n Вы живете в {placeofliving}')

# import math as
# x = int(input())
# t = int(input())

# z = round(((9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - abs(math.sin(t)))) * (math.pow(math.e, x)), 2)
# print(z)


# 1 hw
# import math

# r = int(input())
# print(round(2 * math.pi * r, 2))
# print(round(math.pi * math.pow(r, 2), 2))
# #2 hw
# x = 10
# y = 55
# print(x, y)
# x, y = y, x
# print(x, y)
# #3 hw
# L = int(input())
# g = 9.81
# print((2 * math.pi * math.sqrt(float(L) / g), 2))


# practice lesson 2
# hw 1
# a = float(input())
# b = float(input())
# if b == 0:
#     print('ты на ноль делишь дурак')
# else:
#     print(a / b)
# hw 2
# summa = int(input())
# if summa > 20:
#     print(f'стоимость составила {round(summa - (summa * 0.35), 2)}, ваша скидка 35%')
# else:
#     print('денег мало скидки нет ха')
# hw 3
# a = int(input())
# m = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
# if 1 <= a <= 12:
#     if 9 <= a < 12:
#         print(f'это {m[a]}, осень')
#     elif 3 <= a < 6:
#         print(f'это {m[a]}, весна')
#     elif 6 <= a < 9:
#         print(f'это {m[a]}, лето')
#     else:
#         print(f'это {m[a]}, зима')
# else:
#     print('такого месяца нет(')

# 27.09 cw

# 1
# n = float(input())
# for i in range(1, 11):
#   print(f'{i} килограмм конфет стоит {i * n}')
# 2
# sum = 0
# num = 0
# n = input().split()
# for i in n:
#     sum += int(i)
#     num += 1
# print(f'сумма {sum}, количество чисел {num}')
# 3
# n = [1, '2', 3, 4, '5', '!', 'FF', '5', '7!']
# sum = 0
# for i in n:
#   if str(i).isdigit():
#     sum += int(i)
# print(sum)

# 1 slognaya
# n = int(input())
# ki = ['2', '3', '4']
# for i in range(n + 1):
#   if str(i)[-1] == '1' and i != 11:
#     print(f'{i} овечка')
#   elif str(i)[-1] in ki and not (11 < i < 15):
#     print(f'{i} овечки')
#   else:
#     print(f'{i} овечек')

# 1 овечкА; 2-3-4 овечкИ; 5-6-7-8-9- овечЕК
# 2 slogNaya
# n =  ['Ab', 'AC', 'CD', 'bd', 'te', 'ed']
# lst = []
# for i in n:
#   for j in i:
#     if not j in lst:
#       lst.append(j)
# print(lst)

# 4 10 24
# 1
# text = input().split()
# podhodit = [text[i] for i in range(len(text)) if text[i][0] == 'е' or text[i][0] == 'Е']
# print(len(podhodit))
# 2
# text = input()
# print(text.count(':'), text.replace(':', '%'))
# 3
# text = input()
# print(text.count('.'), text.replace('.', ''))
# 4
# from random import *
# arr = [randint(-100, 100) for i in range(10)]
# for i in range(len(arr) - 1):
#   if arr[i] < 0 and arr[i + 1] < 0:
#     print(f' {arr[i]} и {arr[i + 1]};', end='')
# 5
# n = int(input())
# arr = [int(input()) for i in range(n)]
# print(min(arr), arr.index(min(arr)))
# 6
# from random import *
# arr = [randint(-100, 100) for i in range(8)]
# arrnew = [abs(i * 2)  if i < 15 else i for i in arr]
# print(arr, arrnew)


# 11 10 24
# На занятии

# 1. Ввести одномерный массив A длиной m. Поменять в нём местами первый и последний элементы. Длину массива и его элементы ввести с клавиатуры. В программе описать процедуру для замены элементов массива. Вывести исходные и полученные массивы.
# 2. Даны две дроби A/B и C/D (A, B, C, D - натуральные числа). Составить программу деления дроби на дробь. Ответ должен быть несократимой дробью. Использовать подпрограмму алгоритма Евклида для определения НОД.
# 3. Задана окружность `(x-a)^2 + (y-b)^2 = r^2` и точки P(p1, p2), F(f1, f2), L(l1, l2). Выяснить и вывести на экран, сколько точек и какие лежить внутри окружности. Проверку сформировать в виде процедуры.
# 4. Даны 3 различных массива целых чисел (размер каждого не превышает 15). В каждом массиве найти сумму элементов и среднеарифметическое значение. Маассивы сформировать рандомно.
# 5. Даны катеты двух прямоугольных треугольников. Написать функцию вычисления длины гипотенузы этих треугольников. Сравнить и вывести какая из гипотенуз больше, а какая меньше. Катеты определить рандомно, вывести.
# 6. Натуральное число, в записи которого n цифр, называется числом Армстронга, если сумма его цифр, возведенных в степень n, равна самому числу. Найти все числа Армстронга от 1 до к.

# 1
# from random import *
# def pomenyat(a):
#     a[0], a[-1] = a[-1], a[0]
#     return a

# m = randint(3, 15)
# print(f'нужно ввести {m} значений')
# x = [input() for i in range(m)]
# print(pomenyat(x))

# 2
# def nod(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return b

# def delenie(a, b):
#     a = [int(i) for i in a]
#     b = [int(i) for i in b]
#     resul = f'{a[0] * b[1]}/{a[1] * b[0]}'
#     return resul

# x, y = input().split('/'), input().split('/')
# print(f'несокращенная: {delenie(x, y)}')
# resulnod = nod(int(delenie(x, y)[0]), int(delenie(x, y)[1]))
# if int(delenie(x, y)[1])/resulnod != 1:
#     print(f'сокращенная: {int(delenie(x, y)[0])//resulnod}/{int(delenie(x, y)[1])//resulnod}')
# else:
#     print(f'сокращенная: {int(delenie(x, y)[0])//resulnod}')

# 3
# from random import *
# centrx, centry, r = randint(-10, 10), randint(-10, 10), randint(-10, 10)
# print(centrx, centry, r)
# def proverka(x):
#     if pow((int(x[0])-centrx), 2) + pow((int(x[1])-centry), 2) <= pow(r, 2):
#         return True
#     else:
#         return False

# passed = []
# tochki = [input().split() for i in range(3)]
# for i in tochki:
#     if proverka(i):
#         passed.append(i)
# print(len(passed), passed)

# 4
# from random import *
# def op():
#     spisok = [randint(-100, 100) for i in range(randint(0, 15))]
#     print(f'список, который получился: {spisok}\n сумма элементов:{sum(spisok)}\n среднее значение:{sum(spisok)//len(spisok)}')
# a = [op() for i in range(3)]

# 5
# from random import *
# import math


# def triangle():
#     a, b = randint(0, 100), randint(0, 100)
#     print(f'катеты: {a, b}')
#     c = round(math.sqrt(pow(a, 2) + pow(b, 2)), 3)
#     print(f'гипотенуза равна {c}')
#     return c


# tr = [triangle() for i in range(1, 3)]
# print(f'наибольшая гипотенуза {max(tr)} у треугольника номер {tr.index(
#     max(tr)) + 1}\n наименьшая {min(tr)} у треугольника номер {tr.index(min(tr)) + 1}')

# 6
# from random import *


# def chislo(n):
#     newn = sum([pow(int(i), len(str(n))) for i in str(n)])
#     if n == newn:
#         return True
#     else:
#         return False


# k = randint(0, 1000000)
# podhodit = [i for i in range(k) if chislo(i)]
# print(f'ищем в диапозоне {k} чисел, всего подходящих получилось {len(podhodit)}\n сами числа: {podhodit}')


import matplotlib.pyplot as plt
from matplotlib.ticker import *
from random import *

centrx, centry, r = randint(-100, 100), randint(-100, 100), randint(1, 100)
print(f'центр: ({centrx};{centry}), радиус = {r}')


def pokaz():
    x = [int(tochki[0][0]), int(tochki[1][0]), int(tochki[2][0])]
    y = [int(tochki[0][1]), int(tochki[1][1]), int(tochki[2][1])]

    fig = plt.figure()
    axes = fig.gca()
    axes.set_aspect('equal')

    plt.grid(which='major', linewidth=1)
    plt.grid(which='minor', color='grey', linewidth=0.5)

    axes.xaxis.set_minor_locator(AutoLocator())
    axes.yaxis.set_minor_locator(AutoLocator())

    plt.tick_params(which='major', length=10, width=2)
    plt.tick_params(which='minor', length=5, width=1)

    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)

    plt.xlim(-120, 120)
    plt.ylim(-120, 120)

    circle = plt.Circle((centrx, centry), radius=r, fill=False)
    axes.add_patch(circle)
    circlecentre = plt.Circle(
        (centrx, centry), radius=0.25, fill=True, color='r')
    axes.add_patch(circlecentre)
    plt.scatter(x, y)

    plt.show()


def proverka(x):
    if pow((int(x[0])-centrx), 2) + pow((int(x[1])-centry), 2) <= pow(r, 2):
        return True
    else:
        return False


passed = []
print(f'введите ваши точки:')
tochki = [input().split() for i in range(3)]
for i in tochki:
    if proverka(i):
        passed.append(i)
print(f'{len(passed)} точек подошло, конкретнее: {
      passed}, получившаяся картинка:')

pokaz()

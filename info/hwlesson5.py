# ###Домой

# 1. Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный. Вычисления оформить в виде процедуры.
# 2. Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром, т. е. читается одинаково слева направо и справа налево.

# 1
# from math import *


# def triangle(x):
#     b = list(map(int, [x[0], x[1]]))
#     c = list(map(int, [x[0], 0]))
#     line1 = round(sqrt(pow(b[0], 2) + pow(b[1], 2)))
#     line2 = round(sqrt(pow(c[0], 2) + pow(c[1], 2)))
#     print(f'длины векторов {line1} и {line2}')
#     ugol = ((b[0] * c[0] + b[1] * c[1])/(line1 * line2))
#     print(f'угол относительно оси абцисс {ugol}')
#     return ugol


# tochki = [input().split() for i in range(3)]
# rez = {}
# for i in tochki:
#     rez.update({triangle(i): i})
# print(f'максимальный угол {max(rez.keys())} у точки с координатами {
#       rez.get(max(rez.keys()))}')
# 2
def palindrom(n):
    newn = bin(n)[2:]
    if newn == newn[::-1]:
        return newn
    else: return ''
n = int(input())
rez = {}
for i in range(n + 1):
    if palindrom(i) != '':
        rez.update({i: palindrom(i)})
print(f'найдено чисел палиндромов {len(rez)}, сами числа{rez}')

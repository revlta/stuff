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

#1 slognaya
# n = int(input())
# ki = ['2', '3', '4']
# for i in range(n + 1):
#   if str(i)[-1] == '1' and i != 11:
#     print(f'{i} овечка')
#   elif str(i)[-1] in ki and not (11 < i < 15):
#     print(f'{i} овечки')
#   else:
#     print(f'{i} овечек')

#1 овечкА; 2-3-4 овечкИ; 5-6-7-8-9- овечЕК
#2 slogNaya
n =  ['Ab', 'AC', 'CD', 'bd', 'te', 'ed']
lst = []
for i in n:
  for j in i:
    if not j in lst:
      lst.append(j)
print(lst)

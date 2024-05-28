#coding:utf-8
#задачи на цикл с условием
#Задача №6
N = int(input("Введите натуральное число N: "))
if N <= 0:
    print("Пожалуйста, введите натуральное число больше нуля.")
else:
    for i in range(1, N):
       print(i) 
       
#Задача №7
a = float(input("Введите число a: "))
n = 1
sum_of_fractions = 1.0
while sum_of_fractions <= a:
  n += 1
  sum_of_fractions += 1.0 / n
  print("Наименьшее натуральное число n, для которого выполняется условие 1 + ½ + 1/3 +…+1/n > a, равно:", n)

    

#Задача №8
n = int(input("Введите число n: "))
i = 1
while i**2 <= n:
    i += 1
    print("Первое натуральное число, квадрат которого больше n, равно:", i)
    
#Задача №9
number = 201
while number % 17 != 0:
   number += 1
   print("Минимальное число большее 200, которое нацело делится на 17, равно:", number)
   
#Задача №10
max_number = 0
for i in range(600, -1, -1):  # Правильное задание диапазона до -1, чтобы включить 0
    if i % 28 == 0:
        max_number = i
        break

print("Максимальное натуральное число, не превышающее 600, которое нацело делится на 28, равно:", max_number)

#Задачи на цикл с параметром
#Задача №6
for i in range(2, 42, 2):
    print(i)
    
#Задача №7
for i in range(1, 31, 2):
    print(i)

#Задача №8
import math
for i in range(2, 21):
    print(f"Корень из {i} равен:{math.sqrt(i)}")
    
#Задача №9
price = float(input("Введите цену 1 кг конфет: "))
for weight in range(2, 11):
    total_cost = weight * price
    print(f"Стоимость {weight} кг конфет: {total_cost} руб.")
    
#Задача №10
a = int(input("Введите начало отрезка a: "))
b = int(input("Введите конец отрезка b: "))
if a > b:
    print("Ошибка: начало отрезка должно быть меньше конца отрезка.")
else:
    print("Таблица значений функции y = sqrt(x) на отрезке [", a, ";", b, "]")
    for x in range(int(a), int(b) + 1):
        y = math.sqrt(x)
        print("x =", x, "| y =", y)
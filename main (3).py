#coding:utf-8

#Задача№11
a = int(input("Введите первую скорость в км/ч:"))
b = int(input("Введите вторую скорость в м/с:"))
n = b * 3.6
if a > n:
   print ("Первая скорость больше!")
else:
    print ("Вторая скорость больше!")
    
#Задача№12
r = int(input("Введите радиус круга:")) 
c = int(input("Введите сторону квадрата:")) 
Pi = 3.14
S1 = Pi * r ** 2
S2 = c ** 2
if S1 > S2:
    print ("Площадь круга больше, чем площадь квадрата")
else:
    print ("Площадь квадрата больше, чем площадь круга")
    
#Задача№14
k = int(input("Введите первое значение в мм:")) 
l = int(input("Введите второе значение в дюймах:")) 
m = l * 25.4
if k > m:
    print ("Первое значение больше:")
else:
    print ("Первое значение больше:")
    
#Задача№15
M1 = int(input("Введите массу первого тела:")) 
M2 = int(input("Введите массу второго тела:"))
V1 = int(input("Введите объём первого тела:"))
V2 = int(input("Введите объём второго тела:"))
P1 = V1/M1
P2 = V2/M2
if P1 > P2:
    print ("Плотность первого тела больше!")
else:
    print ("Плотность второго тела больше!")
    

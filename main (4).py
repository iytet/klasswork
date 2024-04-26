#coding:utf-8
#Задача№6
a = int(input("введите длину стороны a:"))
b = int(input("введите длину стороны b:"))
c = int(input("введите длину стороны c:"))
if a == b == c:
    print("равносторонний")
elif (a == b or a == c or b == c) and (a !=b or a !=c or b !=c):
    print("Равнобедренный")
elif a !=b and a !=c and b !=c:
    print("разносторонний")
    
#Задача№7
print("Координаты точки: ")
x = int(input("x = "))
y = int(input("y = "))
if x > 0 and y > 0:
   print("Точка в I четверти")
elif x < 0 and y > 0:
   print("Точка во II четверти")
elif x < 0 and y < 0:
   print("Точка в III четверти")
elif x > 0 and y < 0:
   print("Точка в IV четверти")
elif x == 0 and y == 0:
   print("Точка в центре координат")
elif x == 0:
   print("Точка на оси X")
elif y == 0:
   print("Точка на оси Y")
   
#Задача№8
a = int(input("Введите число месяца a = :"))
if a == '12' or a == '1' or a == '2':
    print('Зима')
elif a == '3' or a == '4' or a == '5':
    print('Весна')
elif a == '6' or a == '7' or a == '8':
    print('Лето')
elif a == '9' or a == '10' or a == '11':  
    print('Осень')
    
    
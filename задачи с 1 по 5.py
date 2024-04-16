#coding:utf-8

#Задача№1
color1 = input("Введите 1 цвет: ")
color2 = input("Введите 2 цвет: ")

if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
    print("фиолетовый")
elif (color1 =="красный" and color2 =="жёлтый ") or (color1 == "жёлтый" and color2 == "красный"):
    print("оранжевый")
elif  (color1 =="синий" and color2 =="жёлтый ") or (color1 == "жёлтый" and color2 == "синий"):
    print("зелёный")
elif color1 == "красный"  and color2 == "красный" :
    print("красный")
elif color1 == "синий"   and color2 == "синий" :
    print("синий")
elif color1 == "жёлтый"   and color2 == "жёлтый" :    
    print("жёлтый")
else: 
    print("Ошибка цвета")
    
#Задача№2
a1 = int(input("Введите целое число a1:"))
b1 = int(input("Введите целое число b1:"))
a2 = int(input("Введите целое число a2:"))
b2 = int(input("Введите целое число b2:"))
a1 = max(a1, a2)
b1 = min(b1, b2)
if a1 < b1:
   print(a1, b1)
elif a1 == b1: 
    print(a)
else:
    print("Пустое множество")

#Задача№3
N = int(input("Введите четырёхзначное число N:"))
sum = 0
while N != 0:
    p = N % 10
    sum = sum + p
    N = N // 10
    print (sum)
    
#Задача№4
k = int(input("Введите значение катета k:"))
l =  int(input("Введите значение катета l:"))
c = (k ** 2 + l ** 2) ** 0.5
print (c) 

#Задача№5
x1 = int(input("Ввести координату x1:"))
y1 = int(input("Ввести координату y1:"))
x2 = int(input("Ввести координату x2:"))
y2 = int(input("Ввести координату y2:"))
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
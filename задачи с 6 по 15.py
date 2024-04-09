#coding:utf-8

#Задача№6
a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
if a > b:
    print(b)
else:
    print(a)
    
#Задача№7
age = int(input("Введите свой возраст:"))
if age <= 13:
    print("детсво")
elif 14 <= age <= 24:       
    print("молодость")   
elif 25 <= age <= 59:
    print("зрелость")
else:
    print("старость")
        
#Задача№8
m1 = int(input("Введите первое число:"))
n1 = int(input("Введите второе число:"))
c1 = int(input("Введите третье число:"))

if m1 > 0:
    m2 = m1
else:
    m2 = 0
if n1 > 0: 
    n2 = n1
else:
    n2 = 0
if c1 > 0: 
    c2 = c1
else:
    c2 = 0
    print( m2 + n2 + c2 )
 
#Задача№9
x = int(input("Введите  число x:"))

if (1000 <= x <= 9999) and (x % 7 == 0 or x % 17 == 0):
    print("YES")
else:
    print("NO")
    
#Задача№10
i = int(input("Введите номер года:"))

if (i % 4 == 0 or i % 400 == 0) and i % 100 != 0:
    print("YES")
else:
    print("NO")
#Задача№11
a1 = int(input( "Введите число a1:"))
b1 = int(input( "Введите число b1:"))
l1 = int(input( "Введите число l1:"))
if a1 == b1 == l1: 
    print("равносторонний")
elif (a1 == b1 or a1 == l1 or b1 == l1) and (a1 !=b1 or a1 !=l1 or b1 !=l1):
    print("равнобедренный")
elif a1 != b1 and a1 != l1 and b1 != l1:
    print("равносторонний")
    
 #Задача№12
a2 = int(input( "Введите число a2:"))
b2 = int(input( "Введите число b2:"))
l2= int(input( "Введите число l2:")) 
if a2 < b2 < l2 or a2 > b2 > l2:
    print(b2)
elif b2 < l2 < a2 or b2 > l2 > a2:
     print(l2)
else:
    print(a2)
    
#Задача№13
y = int(input("Введите порядковый номер месяца y:"))

if y == 2:
    print(28)
elif (x < 8 and x % 2 == 0) or (x > 7 and x % 2 != 0):    
    print(30)
else:
    print(31) 
    
#Задача№14
k = int(input("Введите вес боксёра-любителя k:"))
if k <= 59:
    print("Лёгкий вес")
elif k>=60 and k<=63:
    print("первый полусредний вес")
elif k>=64 and k<=68:    
    print(" Полусредний вес")
   
#Задача№15
g = int(input("Введите целое число g:"))
j = int(input("Введите целое число j:"))
s = (input("Введите строку:"))
if(j == 0 and s == '/'): 
    print("На ноль делить нельзя!")
elif(s == '+'):
    print (g+j)
elif(s == '*'): 
    print (g*j)
elif(s == '/'):
    print (g/j)
elif(s == '-'): 
    print (g-j)
else: 
    print("Неверная операция")

    
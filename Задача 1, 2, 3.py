#coding:utf-8
#Задача №1
a = int(input("Введите целое число a:"))
b = int(input("Введите целое число b:"))
if a > b: 
   print ("Число a больше!")
else:
    print ("Число b больше!")
    
#Задача №2
year = int(input("Введите год:"))
if year % 4 != 0:
    print ("No")
elif year % 100 == 0:
    if year % 400 == 0:
       print ("Yes")
else:
       print ("No")

#Задача №3
n = int(input("Введите число a:"))
    
m = int(input("Введите число m:"))
    
l = int(input("Введите число l:"))
    
if ((n + m) > l) & ((n + l) > m & ((m + l) >n)):
   print ("yes")
else:
    print ("No")
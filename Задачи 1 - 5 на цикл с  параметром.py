#coding:utf-8
#Задачи на цикл с параметром
#Задача №1
INCH_TO_CM = 2.54
for inches in range(10, 23):
  centimeters = inches * INCH_TO_CM
  print(f"{inches} дюймов = {centimeters} сантиметров")
  
#Задача №2
kurs = int(input("Введите курс доллара к рублю: "))
for i in range(1, 21):
    rubles = i * kurs
    print(f"{kurs} долларов = {rubles} рублей")


#Задача №3
import math
e = 1
for n in range(1, 21):
    e *= n
    print(f"e^{n} = {e}")
    
#Задача №4
start = 1 
end = 21
for i in range(start, end + 1):
  print(f"{i}.1")
  
#Задача №5
for i in range(1, 10):
    print(f"2.{i}")

#coding:utf-8
#задача №1
P = int(input("Введите число P: "))
numbers = []
i = 2
while True:
  number = i ** 0.5
  if number < P:
     numbers.append(number)
  else:
       break 
  i += 1       
print("Числа, меньшие", P, "в последовательности корней чисел:")
print(numbers)

#Задача №2
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
if A < B:
  for number in range(A + 1, B):   
      print(number)
else:
    print("Ошибка: A должно быть меньше B.")
    
#Задача №3
A1 = int(input("Введите число A1: "))
B1 = int(input("Введите число B1: "))
if A1 < B1:
   for i in range(B1 -1, A1 -1, -1): 
      print(i)
else:
    print("Ошибка: A должно быть меньше B")
    
#Задача №4
N = int(input("Введите целое число N (> 1): "))
K = (N + 2) // 3
print(f"Наименьшее целое K, при котором 3 * K > N, равно {K}")
print(f"Значение 3 * K: {3 * K}")

#Задача №5
N = int(input("Введите целое число N (> 1): "))
K = (N - 1) // 3
print(f"Наибольшее целое K, при котором 3 * K < N, равно {K}")


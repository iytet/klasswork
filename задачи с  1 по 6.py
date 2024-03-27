#coding:utf-8

#Задача№1
A = int(input("Введите число A, не превышающее по модулю 10000:  "))
B = int(input("Введите число B, не превышающее по модулю 10000:  "))
C = int(input("Введите число C, не превышающее по модулю 10000:  "))
if (A % 2 == 0 and B % 2 != 0) or (A % 2 !=0 and B % 2 == 0):
    print ("YES")
elif (A % 2 == 0 and B % 2 !=0) or (C % 2 !=0 and C % 2 == 0):
    print ("YES") 
elif (B % 2 == 0 and C % 2 !=0) or (B % 2 !=0 and C % 2 == 0):
    print ("YES")
else:    
    print ("NO")     
    
#Задача№2
x = int(input("Введите целое число:"))
if x > 0:
    print(1)
elif x < 0:
    print (-1)
else:
     print (0)
     
#Задача№3
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
if  a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
    print (a, b, с)
    
#Задача№4
A = int(input("Введите целое число A = :"))
B = int(input("Введите целое число B = :"))
C = int(input("Введите целое число C = :"))
X = int(input("Введите целое число X = :"))
Y = int(input("Введите целое число Y = :"))
if A <= X and B <= Y or A <= Y and B <= X:
    print("YES")
else:
    if A > B:
        A, B = B, A
if X > Y:                
 X, Y = Y, X             
if A <= X and B <= Y:   
    print("YES")
else:
    print("NO")
        
#Задача№5
M = int(input("Введите число M = :"))
N = int(input("Введите число N = :"))
K = int(input("Введите число K = :"))
D = int(input("Введите число D = :"))
E = int(input("Введите число E = :"))
if M <= D and N <= E or M <= E and N <= D:
    print("YES") 
elif K <= D and N <= E or K <= E and N <= D:
     print("YES")
elif M <= D and K <= E or M <= E and N <= D:
     print("YES")
else:
     print("YES")
    
#Задача№6
A1 = int(input(" Введите число A1 = : "))
B1 = int(input(" Введите число B1 = : "))
C1 = int(input(" Введите число C1 = : "))
A2 = int(input(" Введите число A2 = : "))
B2 = int(input(" Введите число B2 = : "))
C2 = int(input(" Введите число C2 = : "))
if ((A1 == A2 and B1 == B2 and C1 == C2) or 
(A1 == A2 and B1 == C2 and C1 == B2) or 
(A1 == C2 and B1 == A2 and C1 == B2) or 
(A1 == B2 and B1 == A2 and C1 == C2) or
(A1 == B2 and B1 == C2 and C1 == A2) or 
(A1 == C2 and B1 == B2 and C1 == A2)):
   print('Boxes are equal')
elif ((A1 <= A2 and B1 <= B2 and C1 <= C2) or   
 (A1 <= A2 and B1 <= C2 and C1 <= B2) or
 (A1 <= C2 and B1 <= A2 and C1 <= B2) or
 (A1 <= B2 and B1 <= A2 and C1 <= C2) or
 (A1 <= B2 and B1 <= C2 and C1 <= A2) or
 (A1 <= C2 and B1 <= B2 and C1 <= A2)):
    print('The first box is smaller than the second one')   
elif ((A1 >= A2 and B1 >= B2 and C1 >= C2) or
 (A1 >= A2 and B1 >= C2 and C1 >= B2) or
 (A1 >= C2 and B1 >= A2 and C1 >= B2) or
 (A1 >= B2 and B1 >= A2 and C1 >= C2) or
 (A1 >= B2 and B1 >= C2 and C1 >= A2) or
 (A1 >= C2 and B1 >= B2 and C1 >= A2)):
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')

    
#coding:utf-8

#Задача №1
x = 10
y = 3
z = 13
if x + y==z:
    print("Ответ верный:")
else:
    print("Ответ неверный:")
    
#Задача№2
num = int(input("Какое число я загадал?"))
if num == 5:
    print("Угадал!")
else:
    print("Не угадал!")
    print("Конец игры")
    
if num != 6:
    print("Угадал!")
else:
    print("Не угадал!")
    print("Конец игры")
 
#Задача№3
rain = int(input("На улице идёт дождь?(Введите 1 если да, 0 если нет):"))
if rain == 1:
    print("Пошёл дождь.Возьмите зонтик!")
else:
    print("Дождя нет. Можно выйти на улицу без зонта.")
    
#Задача№4
russian = int(input("Введите количество баллов по русскому языку: "))
math = int(input("Введите количество баллов по математике: "))
informatics = int(input("Введите количество баллов по информатике: "))
total_score = russian + math + informatics
if total_score >= 270:
    print("Поздравляю, ты поступил на бюджет!")
else: 
    print("К сожалению, ты не прошёл на бюджет.")

#Задача №5
number = int(input("Введите число: "))
if number % 2 == 0:
    print("Это четное число. Не забудь использовать зубную нить сегодня!")
else:
    print("Это нечетное число. Сегодня можно отдохнуть от зубной нити.")

#Задача№6
price_1 = float(input("Введите стоимость первого стула: "))
price_2 = float(input("Введите стоимость второго стула: "))
price_3 = float(input("Введите стоимость третьего стула: "))
total_price = price_1 + price_2 + price_3
if total_price > 10000:
    discount = total_price * 0.10
    final_price = total_price - discount
else:
    final_price = total_price
    print(f"Итоговая сумма чека: {final_price} рублей")

#Задача№7
num = int(input("Введите число: "))
if num < 0: 
   num = -num
   print("Модуль числа:", num)

#Задача№8
kostya_cube = int(input("Кубик Кости: "))
owner_cube = int(input("Кубик владельца: "))
if kostya_cube  >= owner_cube:
    difference = kostya_cube - owner_cube
    print ("Сумма: {difference}")
    print ("Костя платит")
else:
   total = kostya_cube + owner_cube
print ("Сумма: {total}")
print ("Владелец платит")
print ("Игра окончена")

#Задача№9
input_amount = int(input("Введите сумму, которую хотите снять: "))
if input_amount % 100 != 0:
   print("Такую сумму снять невозможно. Обратитесь в другой банкомат.")
else:
    print("Вы можете снять указанную сумму.")



worked_hours = int(input("Введите отработанные часы: "))
remaining_loan = float(input("Введите остаток по кредиту: "))
food_expenses = float(input("Введите траты на еду: "))
salary = worked_hours * 200
if salary >= remaining_loan + food_expenses:
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать!")
    
 #Задача№10
mileage = int(input("Введите пробег: "))
day = int(input("Введите сегодняшнее число: "))
sum_digits = sum(int(digit) for digit in str(mileage))
if sum_digits > day:
    print("Сброс.") 
    mileage = 0 
else: 
    print("Сегодня не сломался.")
    print("Пробег:", mileage)


 










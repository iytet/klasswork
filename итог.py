#coding:utf-8
#Задача о погоде
temperature = int(input("Введите температуру (в градусах Цельсия:"))
weather_condition = input("Введите состояние погоды (солнечно, облачно, дождь):")
if temperature > 20  and weather_condition == "солнечно":
      print("Надеть футболку и шорты")
elif temperature > 20 and weather_condition == "облачно":
      print("Надеть джинсы и лёгкую куртку")
elif temperature > 20 and weather_condition == "дождь":
      print("Надеть плащ")
elif temperature <= 20 and weather_condition == "солнечно":
      print("Надеть джинсы и толстовку")
elif temperature <= 20 and weather_condition == "облачно":
      print("Надеть джинсы и водолазку")
elif temperature <= 20 and weather_condition == "дождь":
      print("Надеть джинсы и плащ")
else:
    print("Недостаточно данных для определения одежды")
    
#Задача о книгах
genre = input("Введите жанр книги:")
rating = int(input("Введите рейтинг книги (от 1 до 5): "))
if genre ==  "фантастика" and rating > 4:
     print("Вам стоит прочитать эту книгу!")
else:
     print("Эта книга вам, возможно, не понравится.")

#Задача о бюджете
budget = int(input("Введите Ваш текущий бюджет: "))
price = int(input("Введите цену товара: "))
necessity = input("Необходимость товара (да/нет): ")
if budget >= price:
   if necessity  ==   "да":
     print("Вы можете позволить себе купить этот товар и он необходим.")
   else:
     print("Вы можете позволить себе купить этот товар, но он не является необходимым.")
else:
    if necessity ==  "да":
     print("У Вас недостаточно средств для покупки необходимого товара.")
    else:
     print("У Вас недостаточно средств для покупки этого товара, но он не является необходимым.")
     
#Задача о здоровом питании
calories = int(input("Введите количество калорий в продукте: "))
sugar = int(input("Введите количество сахара в продукте (в граммах): "))
if calories < 200 or sugar < 5:
    print("Этот продукт слишком низкокалорийный или слишком мало содержит сахара. Не рекомендуется покупать.")
elif calories > 500 and sugar > 10:
    print("Этот продукт слишком высококалорийный и содержит много сахара.рекомендуется покупать.")
else:
    print("Этот продукт можно покупать, так как его калорийность и содержание сахара находятся в приемлемых пределах.")
   
#Задача о транспорте
distance = int(input("Введите расстояние до вашего места назначения в километрах:"))
time = int(input("Введите текущее время суток в часах (от 0 до 24): "))
if distance < 2 and (time < 6 or time < 22):
    print("Вам следует идти пешком: ")
elif distance < 10 and (time < 6 or time < 22):
    print("Вам следует использовать велосипед.")
elif distance < 50:
    print("Вам следует использовать автомобиль или общественный транспорт.")
else:
    print("Вам следует использовать автомобиль.")
    
#Задача№1
number = int(input("Введите число: "))
if number >= 0:
  result = number - 10    
else:
  result = number + 10
print("Результат:", result)      
    
#Задача№2
a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
c = a * b
if c < 0:
   result  = c * -2
else:
   result  = c  * 3
print("Результат:", result)
 
#Задача№3
a1 =  int(input("Введите первое число a1: "))
b1 = int(input("Введите второе число b1: "))
sum = a1 + b1
if sum % 2 == 0:
 result = a1 * b1
else:
   if b1 !=0:
     result = a1 / b1
   else:
     print("Ошибка: деление на ноль!")
     result = None
if result is not None:
     print("Результат:", result)
    
#Задача№4
m = int(input("Введите первое число m: "))
n = int(input("Введите второе число n: "))
if m > n:
  result = m - n  
else:
  result = n - m 
print("Результат вычитания:", result)  
    
    
#Задача№5
l = int(input("Введите  число l: "))
if l > 10:
   result = l / 2
else:
   result = l * 5
print("Вывести результат:, result")        
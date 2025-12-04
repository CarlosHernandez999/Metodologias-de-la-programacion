cars = ["audi", "bmw", "chevrolet", "corvette", "tesla"]

for car in cars:

    if cars =="bmw" or car=="tesla" or car=="audi":
        print(car.upper())
    else:
        print(car)

print("\n----Condicional")
# Condicionales: El condicional es el corazon de un if
# Condicional true
car = "bmw"
print(car== "bmw")

# Condicional false
car_2 = "Audi"
print(car_2=="Audi")

# Condicional false
car_2 = "Audi"
print(car_2.lower()=="Audi") # salida: true

# Condicional != para determinar desigualdad
requested_topping = "mushrooms" # -> string
if requested_topping != "anchovies:": # -> true
    print("hold the anchovies")

# comparaciones numericas
age = 18 # variable
print(age==18) # -> true

# Multiple
age_0 = 22
age_1 = 18

print("Multiples condiciones")
print("Operacion or - pseint (o)")
print( age_0>= 21 and age_1>= 21) # True
print( age_0>= 23 and age_1>= 21) # False


age = 19
print(age<21) # true
print(age<=21) # true
print(age>21) # false
print(age>=21) # false

# ¿Como nos preguntamos si un valor esta en una lista?
print("\n A value is in a list")
requested_topping = ["mushrooms", "onions", "pineapple"]
print("mushrooms", requested_topping) # true
print("pepperoni", requested_topping) # false

# A value not in a list
banned_users = ["gabriel", "max", "andrik", "quevedo", "christofer"]
user = "pedro"
print(user not in banned_users)

# Variables de tipos BOOLEANOS
game_active = True
can_edit = False

"""
    if statement

    if condition:
        do something

    if condition:
        do something (true)
    else:
        do something (false)

"""

# Vamos a preguntar la edad del usuario
# y decirle si tiene la edad 
# suficiente para votar
# input() -> str
age = input("Escribe tu edad")
print(f"\n Tu edad es: {age}")

if int(age)>=18:
    print("tu tienes la edad para votar")
else:
    print("lo siento, eres demasiado joven para votar")
try:
    age = int(input("escribe tu edad"))
except: 
    age = -1
    print("error: elemento no valido")

if age < 4:
    print("La entrada es gratuita")
elif age < 18:
        print("La entrada cuesta $200")
elif age > 18:
        print("La entrada cuesta $400")

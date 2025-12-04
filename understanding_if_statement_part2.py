#
try:
    age = int(input("escribe tu edad"))
except:
    age = -1
    print("Error,  ingresaste un caracter no valido")
    if age >= 18:
        print("eres mayor de edad")
    else:
        print("eres menor de edad")
    print("Error, ingresaste un caracter no valido")

print("hola charly")

# bloque if-elif-else 
if age >= 100:
    print("Tienes mas de un silgo")
elif age >= 18 and age < 100:
        print("eres mayor de edad")
elif age >= 0 and age < 18:
        print("eres menor de edad")
else:
    print("tuviste un error")

    age = int(input("escribe tu edad")) 
if age < 4:
    print("La entrada es gratuita")
elif age < 18:
        print("La entrada cuesta $200")
elif age > 18:
        print("La enyrada cuesta $400")

# Utilizando varias listas
guisos_disponibles = ["salsa verde", "deshebrada", "mole"]
guisos_a_ordenar = ["deshebrada", "caldo de iguana"]

print("que guiso desea ordenar")
for guiso in guisos_a_ordenar:
    print(f"Deseo {guiso}")
    if guiso in guisos_disponibles: 
         print(f"si tenemos de ese guiso")
    else:
        print(f"no tenemos de ese guiso")
print("preparando pedido")
"""
    docstring
    un programa que:
        - cuente cuantos numeros ha ingresado el usuario
        - realice la suma de estos numeros
        - me diga cual es el minimo de los numeros ingresados
        - me diga cual es el maximo de los numeros ingresados
"""
counters = 0
sum_numbers = 0.0
minimun = none
maximun = none

while True:
    print("escribe extit para salir")
    user_input = input("ingresa una cantidad (MXN):")

    if user_input == "exit":
        break

    try:
        value = float(user_input)
    except ValueError:
        print("caracter invalido, por favor ingresa un numero")
        continue
    except KeyboardInterrupt:
        print("salida manual")
        break

    counter+=1 # counter = counter + 1 (contador)
    sum_quantities += value # sum_quantitie = sum_quantitie + value (sumador)

    if minimun is None or value < minimun:
        minimun: value

    if minimun is None or value > minimun:
        maximun: value

print("cantidad de numeros ingresados", counter)
print("suma de cantidades", sum_quantities)
print("minimo de cantidades", minimun)
print("maximo de cantidades", maximun)
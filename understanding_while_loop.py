#While infinito
"""
    programa si el usuario escribe un numero
    entre 25 y 50, entonces esta dentro del rango
    y salirme del while
    de otro modo pedirle otro numero.
"""
while True:
    try:
        number = int(input("ingresa un numero"))
        if number <= 25 and number >= 50:
            print("estas dentro del rango")
            break
        else:
            print("estas fuera del rango")
    except ValueError:
        print("introduciste una variable incorrecta")

while True: #while loop infinito
    try:
        number = int(input("ingrese un numero entre 10 y 20"))
    
        if 10 <= number <= 20:
            print("numero dentro del rango, felicitaciones")
            break
        else:
            print("numero fuera del rango")
    except ValueError:
        print("entrada invalida, por favor ingrese un numero entero")
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario")
        break

print("saliste del while")
    

    

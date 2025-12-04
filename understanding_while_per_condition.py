"""
    vamos a realizar un programa que defina un pin para dar acceso
    a un usuario

    El usuario va tener un maximo de intentos para colocar 
    bien el pin

    si usuario sobrepasa este maximo de intentos
    se le va a bloquear la cuenta y el acceso.
"""
CORRECT_PIN = "1234"
MAX_ATTEMPS = 3
attempt = 0

while attempt < MAX_ATTEMPS:

    user_input = input("ingresa tu PIN")

    if user_input == CORRECT_PIN:
        print("acceso concedido")
        break
    else:
        attempt+=1
        remaining_attemps = MAX_ATTEMPS - attempt
        if remaining_attemps < 0:
            print("ingresaste un pin no valido")
            print(f"te quedan {remaining_attemps} intentos")
        else:
            print("cuenta bloqueada")
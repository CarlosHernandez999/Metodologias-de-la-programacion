### FUNCIONES
# Las funciones son bloques de codigo para realizar
# una tarea en especifico

# Cuando queremos realizar la tarea que se ha definido
# en la funcion, tenemos que llamar el nombre de la 
# funcion que realiza la accion

def gretting_christopher():
    print("hello Crikofers")

gretting_christopher()

# Parametros posicionales
def create_full_name(first_name, middle_name, last_name):
    full_name = f"{first_name.strip()} {middle_name.strip()} {last_name.strip()}".title()
    return full_name

first_name = input("dame tu primer nombre:")
middle_name = input("dame tu segundo nombre: (Si no tienes, presiona enter) ")
last_name = input("dame tu apellido:")

# Argumentos posicionales
generated_fullname = create_full_name(first_name.lower(), middle_name.lower(), last_name.lower())
print(generated_fullname)
# args en funciones 
# kwargs en funciones 
# manejo de datos (.txt, csv, json, excel, works, pdf)
# args via consola (sys)
# cli en python - comand line interface
# testing - casos de prueba (borde, validos, invalidos) 
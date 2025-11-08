# Lists
"""
    Las listas nos permiten almacenar informacion
    en un lugar, la cantidad que tenga: ya sean
    pocos elementos o millones de elementos.

    se recomienda nombrar una variable del tipo lista
    en plural.

    En python los corchetes [] definen una lita,
    sus elementos van separados por comas.
    Ejemplo:
"""
bicycles = ["trek", "canondale", "redline", "specialized", "giant"]
print(bicycles)

print(bicycles[0] .title())

# Los indices comienzan en 0 y terminan en n-1, donde n es el numero de elementos
print(bicycles[4] .title())

# Accediendo al ultimo elemento
print(bicycles[-1].title()) # ultimo elemento
print(bicycles[-2].title())
print(bicycles[-5].title()) # primer elemento


# Utilizando valores de la lista.
message = "Mi primer bicicleta fue una" + bicycles[4].upper() + "."
print(message)

message_f = f"Mi primer bicicleta fur una {bicycles[4].title()}." 
print(message_f)

## agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista")
print(bicycles)

print("metodo de las listas para agregar elementos: list_name.append(element)")
bicycles.append("ducatti")

"""
    # LISTAS A-105
    Agregar elementos a una lista
        -append(): agrega un elemento al final de la lista
"""
print("\n--- Agregar elementos a una lista metodo append() ---")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) #salida: ["honda", "yamaha", "suzuki"]
motorcycles.append("ducati")
print(motorcycles) # salida: ["honda", "yamaha", "suzuki", "ducati"]

"""
    Agregar elementos a una lista en una posicion especifica
        -insert(): inserta un elemento en una posicion especifica
"""
print("\n--- Agregar elementos a una lista metodo insert() ---")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki"]
motorcycles.insert(1, "ducati")
print(motorcycles) # salida: ["honda", "ducati", "yamaha", "suzuki"]

"""
    Eliminar elementos de una lista 
        -del(): elimina un elemento en una posicion especifica
"""
print("\n--- Eliminar elementos de una lista metodo del ---")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki"]
del motorcycles[0]
print(motorcycles) # salida: ["yamaha", "suzuki"]

"""
    Eliminar elementos de una lista y usar el valor eliminado
      -pop(): elimina y devuelve el ultimo elemento de la lista 
"""
print("\n--- Eliminar elementos de una lista y usar el valor eliminado metodo pop() ---")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki"]
last_motorcycles = motorcycles.pop()
print(motorcycles) # salida: ["honda", "yamaha"]
print(f" la ultima motocicleta que compre fue {last_motorcycles}.")



"""
    Eliminar elementos especifico de una lista por valor 
      -pop(index): elimina y devuelve el ultimo elemento en la posicion especifica
"""
print("\n--- Eliminar elementos de una lista y usar el valor eliminado metodo pop(index) ---")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki"]
first_motorcycles = motorcycles.pop(1)
print(motorcycles) # salida: ["honda", "suzuki"]
print(f" la primera motocicleta que compre fue {first_motorcycles}.")


"""
    Elimina un elemento especifico de una lista por valor 
      -remove(): elimina la primera aparicion de un valor especifico de una lista
"""
print("\n--- Elimina un elemento especifico de una lista por valor metodo remove ---")
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki", "ducati"]
motorcycles.remove("ducati")
print(motorcycles) # salida: ["honda", "yamaha", "suzuki"]
print("\n")


"""
    Organizar una lista permanente
      - sort(): ordena la lista en orden alfabetico
"""
print("\n--- organizar una lista permanentemente metodo sort() ---")
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki", "ducati"]
motorcycles.sort()
print(motorcycles) # salida: ["ducati", honda", "suzuki", "yamaha",]
print("\n") 

students = ["jesus", "joshue", "andrik", "jen", "miguel", "africa"]
print(students)
desired_students = input("¿que estudiante deseas borrar de la lista?:")
students.remove(desired_students.strip().lower())
print(students)
print("tu has eliminado:",  desired_students)
students.reverse()
print(students)
print(len(students))

cars = ["kia", "ford", "tesla", "volvo", "chevy"]
print(sorted(cars))
sorted_list = sorted(cars)
print("lista original: ", cars)
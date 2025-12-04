# Tuples
"""
    Las tuplas son listas de elementos que no
    cambian de tamaño. Las tuplas son INMUTABLES

    Se utilizan los () para definir la tupla.
"""
rectangle_measurements = (200, 50) # (largo, ancho)
print(rectangle_measurements[0])
print(rectangle_measurements[1])

for measure in rectangle_measurements:
    print(measure)

cars = ["bwm", "porche", "masda"]
print(cars)
cars[0]="bmw"
cars[1]="porshe"
cars[2]="mazda"
print(cars)

rectangle_measurements = (200, 50) # (largo, ancho)
# rectangle_mesurements[0]=300 #no se puede
# rectangle_mesurements[1]=100 #no se puede
rectangle_measurements = (300, 100)

"""
    no podemos modificar una tupla directamente,
    lo que si podemos hacer es cambiar la asignacion
    a una variable que almacena una tupla.
"""
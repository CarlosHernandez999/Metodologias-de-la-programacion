# whitespaces
"""
un Whitespace se refiere a cualquier caracter que no
se imprime, es decir, un espacio, tabuladores y
finales de linea. Los whitespace se utilizan 
comunmente para organizar las salidas de tal manera
que sea mas amigable de leer o ver para el usuario

Ejemplo
    - Tabulador: \t
    - Salto de linea: \n
"""
print("Whitespace Tabulador")
print("Python")
print("\tPython")
print("\t\tPython")

Print("Whitespace Salto De Linea")
Print("lenguages: \n\tPython\nC\n\tJavascript")


# Eliminacion de espacios en blanco
programming_lenguage = " python "
print(programming_lenguage)
print(programming_lenguage.rstrip())
print(programming_lenguage.lstrip())
print(programming_lenguage.strip())

# Syntax Error con Strings
message = 'una fortaleza de python es su comunidad'
print(message)
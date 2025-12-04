covenant_grunt = {
    "color": "orange",
    "weapon": "plasma gun",
    "armament": "plasma-granade",
    "healt": 2
}

covenant_elite = {
    "color": "green",
    "weapon": "plasma gun",
    "armament": "plasma-granade",
    "healt": 7
}

covenant_jackal = {
    "color": "gray",
    "weapon": "plasma gun",
    "armament": "plasma-granade",
    "healt": 7
}

#Lista de diccionario
covenant =[ncovenant_grunt, covenant_elite, covenant_jackal]

for covenant in covenants:
    print("\n" covenants)
    for key, value in covenant.items():
        print(key + value)
        print()

## Diccionario de diccionarios
sensors = {
    "temperature":{
        "id": "temp_1",
        "location": "aula 105",
        "value": 60,
        "unit": "percentaje"
    },
    "humedad":{
        "id": "hum_1",
        "location": "aula 105",
        "value": 60,
        "unit": "percentaje"
    }
}

print("temperatura")
print(sensors["humedad"]["value"])
print(ubicacion)
print()
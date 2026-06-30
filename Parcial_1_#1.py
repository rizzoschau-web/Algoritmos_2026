# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.

heroes = ["Spiderman",
          "Iron Man",
          "Capitan America",
          "Groot",
          "Storm",
          "Black Widow",
          "Deadpool",
          "Thor",
          "Hawkeye",
          "Squirrel Girl",
          "Vision",
          "Hulk",
          "Rogue",
          "Magneto",
          "Gambit" ]

def buscar_cap(heroes: list, indice: ind = 0) -> bool: 
    if indice >= len(heroes):
        return False
    if heroes[indice] == "Capitan America":
        return True
    return buscar_cap(heroes, indice + 1)

def listado(heroes: list, indice: ind = 0) -> None:
    if indice >= len(heroes):
        return
    print(f"{indice + 1:>2}. {heroes[indice]}")
    listado(heroes, indice + 1)

print("lista de 15 heroes: ")
listado(heroes)

print("¿Capitan America se encuentra en la lista? ")
found = buscar_cap(heroes)
print("Capitan America se encuentra en la lista." if found else "Capitan America no se enecuentra en la lista")

# Corregir el Print.
# Terminado.
superheroes = [
    "Spider-Man",
    "Iron Man",
    "Capitán America",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Doctor Strange",
    "Black Panther",
    "Wolverine",
    "Wanda Maximoff",
    "Ant-Man",
    "Star-Lord",
    "Groot",
    "Rocket Raccoon",
]
 
 
def buscar_recursivo(lista, valor_buscado, indice=0):
    if indice == len(lista):
        return False
 
    if lista[indice] == valor_buscado:
        return True
 
    return buscar_recursivo(lista, valor_buscado, indice + 1)
 
 
def listar_recursivo(lista, indice=0):
    if indice == len(lista):
        return
 
    print(lista[indice])
    listar_recursivo(lista, indice + 1)
 
 
if __name__ == "__main__":
    print("Listado recursivo de superheroes:")
    listar_recursivo(superheroes)
 
    print()
    esta = buscar_recursivo(superheroes, "Capitán America")
    if esta:
        print("Capitán America SI está en la lista")
    else:
        print("Capitán America NO está en la lista")
 
    print()
    # prueba con alguien que no está
    esta_thanos = buscar_recursivo(superheroes, "Thanos")
    print(f"¿Está Thanos en la lista? {esta_thanos}")
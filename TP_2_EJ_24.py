#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:
#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
#ción uno la cima de la pila;[86]
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

def crear_pila():
    return []

def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    if not pila_vacia(pila):
        return pila.pop()
    return None

def pila_vacia(pila):
    return len(pila) == 0

def cargar_pila():
    pila = crear_pila()
    pj = [
        ("Thor", 8),
        ("Black Widow", 9),
        ("Groot", 6),
        ("Dr. Strange", 6),
        ("Rocket Raccoon", 7),
        ("Luna Snow", 0),
        ("Phoenix", 5),
        ("Iron Man", 10),
        ("Mantis", 5),
        ("Ultron", 1),
        ("Hela", 1),
        ("Gambito", 1), # No cuento el cameo en la ultima peli de Deapool.
    ]
    for p in pj:
        apilar(pila, p)
    return pila

def pos_rocket_groot(pila):
    aux = crear_pila()
    posicion = 1
    pos_rocket, pos_groot = None, None

    while not pila_vacia(pila):
        nombre, peliculas = desapilar(pila)
        if nombre == "Rocket Raccoon":
            pos_rocket = posicion
        if nombre == "Groot":
            pos_groot = posicion
        apilar(aux, (nombre, peliculas))
        posicion += 1

    while not pila_vacia(aux):
        apilar(pila, desapilar(aux))

    return {"Rocket Raccoon": pos_rocket, "Groot": pos_groot}

def pj_5_pelis(pila):
    aux = crear_pila()
    resultado = []

    while not pila_vacia(pila):
        elemento = desapilar(pila)
        nombre, peliculas = elemento
        if peliculas > 5:
            resultado.append(elemento)
        apilar(aux, elemento)

    while not pila_vacia(aux):
        apilar(pila, desapilar(aux))

    return resultado

def pelis_bw(pila):
    aux = crear_pila()
    cantidad = None

    while not pila_vacia(pila):
        elemento = desapilar(pila)
        nombre, peliculas = elemento
        if nombre == "Black Widow":
            cantidad = peliculas
        apilar(aux, elemento)

    while not pila_vacia(aux):
        apilar(pila, desapilar(aux))

    return cantidad

def pj_CDG(pila):
    aux = crear_pila()
    resultado = []
    letras = ('C', 'D', 'G')

    while not pila_vacia(pila):
        elemento = desapilar(pila)
        nombre, peliculas = elemento
        if nombre.startswith(letras):
            resultado.append(elemento)
        apilar(aux, elemento)

        while not pila_vacia(aux):
            apilar(pila, desapilar(aux))

        return resultado
    
def main():
    pila = cargar_pila()

    print ("Posición de Rocket Raccoon y Groot: ")
    posiciones = pos_rocket_groot(pila)
    for personaje, pos in posiciones.items():
        if pos:
            print(f"{personaje}: posición {pos}")
        else:
            print(f"{personaje}: No se encontró en la pila.")

    print("Películas de Black Widow: ")
    cantidad_bw = pelis_bw(pila)
    if cantidad_bw is not None:
        print (f"Black Widow ha paericipado en {cantidad_bw} películas.")
    else:
        print("Black Widow no se encontró en la pila.")

    print("Personajes empezados por C, D o G")
    resultado_d = pj_CDG(pila)
    if resultado_d:
        for nombre, peliculas in resultado_d:
            print(f"{nombre} ({peliculas} películas)")
        
        else: 
            print(" No hay pesronajes que empiecen por C, D O G")

if __name__ == "__main__":
    main()
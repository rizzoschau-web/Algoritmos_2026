#20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
#cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
#norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
#que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
#partida, retornando por el mismo camino que fue.

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

opuesto = {
    "norte"    : "sur",
    "sur"      : "norte",
    "este"     : "oeste",
    "oeste"    : "este",
    "noreste"  : "suroeste",
    "noroeste" : "sureste",
    "sureste"  : "noroeste",
    "suroeste" : "noreste",
}

def registrar_movimientos():
     pila = crear_pila()
    print("Direcciones válidas: ")
    print("norte, sur, este, oeste, noreste, noroeste, sureste, suroeste")
    print("Ingrese 'fin' para terminar.")

while True:
        direccion = input("Dirección: ").strip().lower()
 
        if direccion == "fin":
            break
 
        if direccion not in opuesto:
            print("Dirección no válida, intentar de nuevo.")
            continue
 
        try:
            pasos = int(input("Cantidad de pasos: "))
            if pasos <= 0:
                print("Los pasos deben ser un número positivo.")
                continue
        except ValueError:
            print("Ingrese un número entero.")
            continue
 
        apilar(pila, (pasos, direccion))
        print(f"Movimiento registrado: {pasos} pasos al {direccion}")
 
    return pila

def generar_regreso(pila_movimientos):
    pila_regreso = crear_pila()
 
    while not pila_vacia(pila_movimientos):
        pasos, direccion = desapilar(pila_movimientos)
        direccion_vuelta = opuesto[direccion]
        apilar(pila_regreso, (pasos, direccion_vuelta))
 
    return pila_regreso

def mostrar_pila(pila, titulo):
    aux = crear_pila()
 
    print(titulo)
    paso_num = 1
 
    while not pila_vacia(pila):
        pasos, direccion = desapilar(pila)
        print(f"Paso {paso_num}: {pasos} pasos al {direccion}")
        apilar(aux, (pasos, direccion))
        paso_num += 1
 
    while not pila_vacia(aux):
        apilar(pila, desapilar(aux))

def main():
    print("Registro de Movimientos")

    pila_ida = registrar_movimientos()
 
    if pila_vacia(pila_ida):
        print("No se registró ningún movimiento.")
        return
    
    print()
    mostrar_pila(pila_ida, "Movimientos registrados de ida: ")
    pila_vuelta = generar_regreso(pila_ida)
    print()
    mostrar_pila(pila_vuelta, "Secuencia de regreso: ")
    print()
    print("El robot volvió al punto de partida.")

    if __name__ == "__main__":
    main()
from graph import Graph
from heap import HeapMin
from datos_casa import ambientes, conexiones

casa = Graph(is_dir=False)

print('\na) Ambientes de la casa:')
for nombre in ambientes:
    casa.add_vertex(nombre)
    print('Se registró:', nombre)

print('\nb) Conexiones entre ambientes (distancias en metros):')
for origen, destino, metros in conexiones:
    casa.add_edge(metros, origen, destino)
    print(f'{origen} <-> {destino}: {metros} m')

print('\nCantidad de conexiones por ambiente:')
for vertice in casa:
    print(f'{vertice.value}: {len(vertice.edges)} conexiones')

print('\nc) Árbol de expansión mínima (Kruskal):')
arbol_minimo = casa.kruskal('Cocina')
metros_totales = 0
cantidad_aristas = 0
for arista in arbol_minimo.split(';'):
    origen, destino, metros = arista.rsplit('-', 2)
    metros = int(metros)
    print(f'{origen} <-> {destino}: {metros} m')
    metros_totales += metros
    cantidad_aristas += 1
print(f'Total de cable para conectar todos los ambientes: {metros_totales} metros')
print(f'Cantidad de enlaces en el árbol mínimo: {cantidad_aristas}')

print('\nd) Camino más corto de Habitación 1 a Sala de estar:')
inicio = 'Habitación 1'
fin = 'Sala de estar'
distancias = {vertice.value: float('inf') for vertice in casa}
anteriores = {}
distancias[inicio] = 0
pendientes = HeapMin()
pendientes.arrive(inicio, 0)

while pendientes.size() > 0:
    costo, actual = pendientes.attention()
    if costo > distancias[actual]:
        continue
    if actual == fin:
        break

    posicion = casa.search(actual, 'value')
    vertice = casa[posicion]
    for arista in vertice.edges:
        nuevo_costo = costo + arista.weight
        if nuevo_costo < distancias[arista.destination]:
            distancias[arista.destination] = nuevo_costo
            anteriores[arista.destination] = actual
            pendientes.arrive(arista.destination, nuevo_costo)

if distancias[fin] == float('inf'):
    print('No existe un camino entre esos ambientes.')
else:
    camino = [fin]
    actual = fin
    while actual != inicio:
        actual = anteriores[actual]
        camino.insert(0, actual)
    print('Recorrido:', ' -> '.join(camino))
    print(f'Cable necesario entre router y Smart TV: {distancias[fin]} metros')

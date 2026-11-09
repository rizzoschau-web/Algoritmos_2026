from graph import Graph
from datos_red import equipos, conexiones
from heap import HeapMin

red = Graph(is_dir=False)

print('a) Carga de equipos:')
for nombre, tipo in equipos:
    red.add_vertex(nombre, tipo)
    print(f'Se registró {nombre} como {tipo}.')

for origen, destino, peso in conexiones:
    red.add_edge(peso, origen, destino)


print('\nb) Barrido en profundidad y amplitud desde las notebooks:')
for equipo in ('Red Hat', 'Debian', 'Arch'):
    print(f'\nDesde {equipo} en profundidad:')
    red.deep_show(equipo)
    print(f'Desde {equipo} en amplitud:')
    red.amplitude_show(equipo)

print("\nc) Caminos más cortos para imprimir:")
for origen in ["Manjaro", "Red Hat", "Fedora"]:

    distancias = {vertice.value: float("inf") for vertice in red}
    anteriores = {}

    distancias[origen] = 0

    pendientes = HeapMin()
    pendientes.arrive(origen, 0)

    while pendientes.size() > 0:
        costo, actual = pendientes.attention()

        if costo > distancias[actual]:
            continue

        posicion = red.search(actual, "value")
        vertice = red[posicion]

        for arista in vertice.edges:
            destino = arista.destination
            nuevo_costo = costo + arista.weight

            if nuevo_costo < distancias[destino]:
                distancias[destino] = nuevo_costo
                anteriores[destino] = actual
                pendientes.arrive(destino, nuevo_costo)
    camino = []
    actual = "Impresora"

    if distancias[actual] != float("inf"):
        while actual != origen:
            camino.insert(0, actual)
            actual = anteriores[actual]
        camino.insert(0, origen)
        print(f"{origen}: {' -> '.join(camino)} | costo: {distancias['Impresora']}")
    else:
        print(f"{origen}: No existe camino hasta la impresora")

print('\nd) Árbol de expansión mínima (Kruskal):')
resultado = red.kruskal('Router 1')
costo_total = 0
for arista in resultado.split(';'):
    origen, destino, peso = arista.rsplit('-', 2)
    costo_total += int(peso)
    print(f'{origen} -- {destino}: {peso}')
print(f'Peso total: {costo_total}')

print("\ne) PC con camino más corto hasta Guaraní:")
mejor_pc = None
menor_costo = float("inf")
for vertice in red:
    if vertice.other_values == "pc":
        origen = vertice.value
        distancias = {nodo.value: float("inf") for nodo in red}
        distancias[origen] = 0
        pendientes = HeapMin()
        pendientes.arrive(origen, 0)
        
        while pendientes.size() > 0:
            costo, actual = pendientes.attention()
            if costo > distancias[actual]:
                continue
            posicion = red.search(actual, "value")
            nodo = red[posicion]
            for arista in nodo.edges:
                destino = arista.destination
                nuevo_costo = costo + arista.weight
                if nuevo_costo < distancias[destino]:
                    distancias[destino] = nuevo_costo
                    pendientes.arrive(destino, nuevo_costo)
        if distancias["Guaraní"] < menor_costo:
            menor_costo = distancias["Guaraní"]
            mejor_pc = origen

print(f"{mejor_pc}: costo {menor_costo}")

print('\nf) Computadora conectada al Switch 1 más cercana a MongoDB:')
mejor_equipo = None
menor_costo = float('inf')
for equipo in ('Debian', 'Ubuntu', 'Mint'):
    pendientes = red.dijkstra(equipo)
    while pendientes.size() > 0:
        actual, costo, anterior = pendientes.pop()
        if actual == 'MongoDB' and costo < menor_costo:
            menor_costo = costo
            mejor_equipo = equipo
print(f'{mejor_equipo}: costo {menor_costo}')

print('\ng) Se cambia la impresora del Switch 1 al Router 2:')
red.delete_edge('Impresora', 'Switch 1')
red.add_edge(22, 'Impresora', 'Router 2')
print('Conexión actual: Impresora -- Router 2 (peso supuesto: 22)')
print('Se repite el recorrido del punto b:')
for equipo in ('Red Hat', 'Debian', 'Arch'):
    print(f'\nDesde {equipo} en profundidad:')
    red.deep_show(equipo)
    print(f'Desde {equipo} en amplitud:')
    red.amplitude_show(equipo)

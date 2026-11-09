from tree import BinaryTree
from personajes_marvel import personajes

marvel = BinaryTree()
print('a) Registro de personajes:')
for nombre, es_heroe in personajes:
    marvel.insert_node(nombre, es_heroe)
    if es_heroe:
        print(f'Se ha registrado a {nombre} como Héroe.')
    else:
        print(f'Se ha registrado a {nombre} como Villano.')

nodos = []
pila = []
actual = marvel.root
while actual is not None or pila:
    while actual is not None:
        pila.append(actual)
        actual = actual.left
    actual = pila.pop()
    nodos.append(actual)
    actual = actual.right

print('\nb) Villanos ordenados alfabeticamente:')
for nodo in nodos:
    if nodo.other_values is False:
        print(nodo.value)

print('\nc) Superhéroes que empiezan con C:')
for nodo in nodos:
    if nodo.other_values is True and nodo.value.startswith('C'):
        print(nodo.value)

contador_heroes = 0
for nodo in nodos:
    if nodo.other_values is True:
        contador_heroes += 1
print('\nd) Cantidad de superhéroes:', contador_heroes)


print('\ne) Búsqueda por proximidad y corrección del nombre:')
busqueda = input('Ingresá el nombre o una parte del nombre: ').strip()

coincidencias = []
if busqueda:
    for nodo in nodos:
        if busqueda.lower() in nodo.value.lower():
            coincidencias.append(nodo)

if not busqueda:
    print('No ingresaste ningún texto para buscar.')
elif not coincidencias:
    print('No se encontraron personajes que coincidan.')
else:
    print('Coincidencias encontradas:')
    for numero, nodo in enumerate(coincidencias, start=1):
        print(f'{numero}. {nodo.value}')

    opcion = input('Ingresá el número del personaje que querés corregir: ').strip()
    if opcion.isdigit() and 1 <= int(opcion) <= len(coincidencias):
        elegido = coincidencias[int(opcion) - 1]
        nombre_nuevo = input(f'Ingresá el nombre correcto de {elegido.value}: ').strip()
        if not nombre_nuevo:
            print('No se ingresó un nombre nuevo. No se modificó el árbol.')
        elif nombre_nuevo != elegido.value and marvel.search(nombre_nuevo) is not None:
            print('Ya existe un personaje con ese nombre. No se modificó el árbol.')
        elif nombre_nuevo == elegido.value:
            print('El nombre ingresado es igual al actual.')
        else:
            nombre_anterior = elegido.value
            arbol_corregido = BinaryTree()
            for nodo in nodos:
                nombre = nombre_nuevo if nodo.value == nombre_anterior else nodo.value
                arbol_corregido.insert_node(nombre, nodo.other_values)
            marvel = arbol_corregido
            print(f'Nombre modificado: {nombre_anterior} -> {nombre_nuevo}')
    else:
        print('Opción inválida. No se modificó el árbol.')


print('\nf) Superhéroes en orden descendente:')
pila = []
actual = marvel.root
while actual is not None or pila:
    while actual is not None:
        pila.append(actual)
        actual = actual.right
    actual = pila.pop()
    if actual.other_values is True:
        print(actual.value)
    actual = actual.left

print('\ng) Bosque de dos árboles:')
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

pila = [marvel.root]
while pila:
    nodo = pila.pop()
    if nodo is not None:
        if nodo.other_values is True:
            arbol_heroes.insert_node(nodo.value, True)
        else:
            arbol_villanos.insert_node(nodo.value, False)
        pila.append(nodo.right)
        pila.append(nodo.left)

for titulo, arbol in [('Héroes', arbol_heroes), ('Villanos', arbol_villanos)]:
    cantidad = 0
    pila = [arbol.root]
    while pila:
        nodo = pila.pop()
        if nodo is not None:
            cantidad += 1
            pila.append(nodo.left)
            pila.append(nodo.right)
    print(f'I. Cantidad de nodos de {titulo}: {cantidad}')

for titulo, arbol in [('Héroes', arbol_heroes), ('Villanos', arbol_villanos)]:
    print(f'\nII. {titulo} en orden alfabético:')
    pila = []
    actual = arbol.root
    while actual is not None or pila:
        while actual is not None:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        print(actual.value)
        actual = actual.right

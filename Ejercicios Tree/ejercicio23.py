from tree import BinaryTree
from queue_ import Queue
from datos_criaturas import criaturas

arbol = BinaryTree()

for nombre, derrotado_por in criaturas:
    arbol.insert_node(nombre, {
        'derrotado_por': derrotado_por,
        'descripcion': '',
        'capturada': None,
        'observacion': ''
    })

print('a) Criaturas y quien las derrotó (inorden):')
pila = []
actual = arbol.root
while actual is not None or pila:
    while actual is not None:
        pila.append(actual)
        actual = actual.left
    actual = pila.pop()
    print(actual.value, '- Derrotado por:', actual.other_values['derrotado_por'] or 'Nadie')
    actual = actual.right

print('\nb) Cargar una descripción:')
nombre_buscado = input('Ingresá el nombre exacto de la criatura: ').strip()
nodo = arbol.search(nombre_buscado)
if nodo is not None:
    descripcion = input(f'Ingresá una breve descripción de {nodo.value}: ').strip()
    if descripcion:
        nodo.other_values['descripcion'] = descripcion
        print(f'Descripción registrada para {nodo.value}.')
    else:
        print('No se ingresó ninguna descripción.')
else:
    print('No se encontró esa criatura.')

print('\nc) Información de Talos:')
nodo = arbol.search('Talos')
if nodo is not None:
    print('Nombre:', nodo.value)
    print('Derrotado por:', nodo.other_values['derrotado_por'] or 'Nadie')
    print('Descripción:', nodo.other_values['descripcion'] or 'Sin descripción')
    print('Capturada por:', nodo.other_values['capturada'] or 'Nadie')
    print('Observación:', nodo.other_values['observacion'] or 'Sin observaciones')

print('\nd) Tres héroes/dioses que derrotaron más criaturas:')
conteo = {}
pendientes = Queue()
if arbol.root is not None:
    pendientes.arrive(arbol.root)
while pendientes.size() > 0:
    nodo = pendientes.attention()
    nombre = nodo.other_values['derrotado_por']
    if nombre is not None:
        conteo[nombre] = conteo.get(nombre, 0) + 1
    if nodo.left is not None:
        pendientes.arrive(nodo.left)
    if nodo.right is not None:
        pendientes.arrive(nodo.right)
for heroe, cantidad in sorted(conteo.items(), key=lambda par: (-par[1], par[0]))[:3]:
    print(heroe, '-', cantidad)

print('\ne) Criaturas derrotadas por Heracles:')
pila = []
actual = arbol.root
while actual is not None or pila:
    while actual is not None:
        pila.append(actual)
        actual = actual.left
    actual = pila.pop()
    if actual.other_values['derrotado_por'] == 'Heracles':
        print(actual.value)
    actual = actual.right

print('\nf) Criaturas no derrotadas:')
pila = []
actual = arbol.root
while actual is not None or pila:
    while actual is not None:
        pila.append(actual)
        actual = actual.left
    actual = pila.pop()
    if actual.other_values['derrotado_por'] is None:
        print(actual.value)
    actual = actual.right

print('\ng) Campo capturada:')
print('Todas las criaturas tienen el campo capturada (inicialmente None).')

print('\nh) Capturas de Heracles:')
for nombre in ('Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto'):
    nodo = arbol.search(nombre)
    if nodo is not None:
        nodo.other_values['capturada'] = 'Heracles'
        print(nombre, '- capturada por Heracles')

print('\ni) Búsqueda por coincidencia:')
busqueda = input('Ingresá un nombre o parte del nombre de una criatura: ').strip()
if busqueda:
    pila = []
    actual = arbol.root
    encontrados = 0
    while actual is not None or pila:
        while actual is not None:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        if busqueda.casefold() in actual.value.casefold():
            print('Coincidencia encontrada:', actual.value)
            encontrados += 1
        actual = actual.right
    if encontrados == 0:
        print('No se encontraron coincidencias.')
else:
    print('No ingresaste ningún texto para buscar.')

print('\nj) Eliminar Basilisco y Sirenas:')
datos = {}
pendientes = Queue()
if arbol.root is not None:
    pendientes.arrive(arbol.root)
while pendientes.size() > 0:
    nodo = pendientes.attention()
    datos[nodo.value] = nodo.other_values.copy()
    if nodo.left is not None:
        pendientes.arrive(nodo.left)
    if nodo.right is not None:
        pendientes.arrive(nodo.right)
for nombre in ('Basilisco', 'Sirenas'):
    if arbol.search(nombre) is not None:
        arbol.delete_node(nombre)
        datos.pop(nombre)
        print('Eliminada:', nombre)
pendientes = Queue()
if arbol.root is not None:
    pendientes.arrive(arbol.root)
while pendientes.size() > 0:
    nodo = pendientes.attention()
    nodo.other_values = datos[nodo.value]
    if nodo.left is not None:
        pendientes.arrive(nodo.left)
    if nodo.right is not None:
        pendientes.arrive(nodo.right)

print('\nk) Aves del Estínfalo:')
nodo = arbol.search('Aves del Estínfalo')
if nodo is not None:
    nodo.other_values['derrotado_por'] = 'Heracles'
    nodo.other_values['observacion'] = 'Heracles derrotó a varias aves.'
    print(nodo.value, '-', nodo.other_values['observacion'])

print('\nl) Cambiar Ladón por Dragón Ladón:')
nodo = arbol.search('Ladón')
if nodo is not None:
    info_ladon = nodo.other_values.copy()
    datos = {}
    pendientes = Queue()
    pendientes.arrive(arbol.root)
    while pendientes.size() > 0:
        actual = pendientes.attention()
        datos[actual.value] = actual.other_values.copy()
        if actual.left is not None:
            pendientes.arrive(actual.left)
        if actual.right is not None:
            pendientes.arrive(actual.right)
    arbol.delete_node('Ladón')
    datos.pop('Ladón')
    pendientes = Queue()
    if arbol.root is not None:
        pendientes.arrive(arbol.root)
    while pendientes.size() > 0:
        actual = pendientes.attention()
        actual.other_values = datos[actual.value]
        if actual.left is not None:
            pendientes.arrive(actual.left)
        if actual.right is not None:
            pendientes.arrive(actual.right)
    arbol.insert_node('Dragón Ladón', info_ladon)
    print('Ladón -> Dragón Ladón')

print('\nm) Recorrido por nivel:')
arbol.by_level()

print('\nn) Criaturas capturadas por Heracles:')
pila = []
actual = arbol.root
while actual is not None or pila:
    while actual is not None:
        pila.append(actual)
        actual = actual.left
    actual = pila.pop()
    if actual.other_values['capturada'] == 'Heracles':
        print(actual.value)
    actual = actual.right

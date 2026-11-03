# Parcial 2, Ejercicio 1, Algoritmos, Walter Bel

from tree import BinaryTree
from pokemon_data import pokemons

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['nombre'], pokemon)
    arbol_numero.insert_node(pokemon['numero'], pokemon)
    for tipo in pokemon['tipos']:
        arbol_tipo.insert_node(tipo, pokemon)


def obtener_nodos(root, lista):
    if root is not None:
        obtener_nodos(root.left, lista)
        lista.append(root)
        obtener_nodos(root.right, lista)


nodos_nombre = []
obtener_nodos(arbol_nombre.root, nodos_nombre)
nodos_numero = []
obtener_nodos(arbol_numero.root, nodos_numero)
nodos_tipo = []
obtener_nodos(arbol_tipo.root, nodos_tipo)

# 1. Mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;

# SDatos de un Pokémon por número
print('--- Búsqueda por número ---')
numero = int(input('ingrese el número del pokémon: '))
nodo = arbol_numero.search(numero)
if nodo is not None:
    print(nodo.other_values)
else:
    print('No encontrado, número fuera de rango.')

# Datos de un Pokémon por nombre (proximidad)
print('--- Búsqueda por nombre (proximidad) ---')
texto = input('ingrese el nombre o parte del nombre: ').lower()
for nodo in nodos_nombre:
    if texto in nodo.value.lower():
        print(nodo.other_values)
else:
    print('No encontrado.')

# 2. Mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
print('--- Pokémons por tipo ---')
for tipo in ['fantasma', 'fuego', 'acero', 'electrico']:
    print(f'Tipo {tipo}:')
    for nodo in nodos_tipo:
        if nodo.value == tipo:
            print(nodo.other_values['nombre'])

# 3. Realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;

print('--- Listado ascendente por nombre ---')
arbol_nombre.inorden()

print('--- Listado por nivel por nombre ---')
arbol_nombre.by_level()

# 4. Mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
print('--- Débiles frente a Jolteon, Lycanroc y Tyrantrum ---')
for nombre in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    atacante = arbol_nombre.search(nombre)
    if atacante is not None:
        print(f'Débiles frente a {nombre}:')
        for nodo in nodos_nombre:
            for tipo in atacante.other_values['tipos']:
                if tipo in nodo.other_values['debilidades']:
                    print(nodo.value)
                    break

# 5. Mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
print('--- Cantidad de Pokémons por tipo ---')
cantidad_por_tipo = {}
for nodo in nodos_tipo:
    if nodo.value in cantidad_por_tipo:
        cantidad_por_tipo[nodo.value] += 1
    else:
        cantidad_por_tipo[nodo.value] = 1
for tipo in cantidad_por_tipo:
    print(tipo, cantidad_por_tipo[tipo])

# 6. Determinar cuantos Pokémons tienen megaevolucion.
print('--- Pokémons con megaevolución ---')
cantidad_mega = 0
for nodo in nodos_nombre:
    if nodo.other_values['mega']:
        cantidad_mega += 1
print(cantidad_mega)

# 7. Determinar cuantos Pokémons tiene forma gigamax.
print('--- Pokémons con forma gigamax ---')
cantidad_gigamax = 0
for nodo in nodos_nombre:
    if nodo.other_values['gigamax']:
        cantidad_gigamax += 1
print(cantidad_gigamax)
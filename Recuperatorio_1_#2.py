from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes

# ====================================================================================#
class Personaje:
    def __init__(self, nombre, alias, nombre_real, bio, anio, es_villano):
        self.name = nombre
        self.alias = alias
        self.real_name = nombre_real if nombre_real is not None else "Desconocido"
        self.bio = bio
        self.year = anio
        self.is_villain = es_villano

    def tipo(self):
        return 'villano' if self.is_villain else 'heroe'

    def __str__(self):
        return f"{self.name} ({self.real_name}) - {self.year} - {self.tipo()}"

# ====================================================================================#
def by_name(item):
    return item.name

def by_real_name(item):
    return item.real_name

def by_year(item):
    return item.year

def build_list(items):
    lista = List()
    lista.add_criterion('name', by_name)
    lista.add_criterion('real_name', by_real_name)
    lista.add_criterion('year', by_year)
    for hero in items:
        lista.append(Personaje(hero['name'], hero['alias'], hero['real_name'],
                                hero['short_bio'], hero['first_appearance'], hero['is_villain']))
    return lista

def separador(titulo):
    print()
    print('=' * 70)
    print(titulo)
    print('=' * 70)

# ====================================================================================#
personajes = build_list(superheroes)
print(f'Total de personajes cargados: {personajes.size()}')

# ====================================================================================#
separador('1) Listado ascendente por nombre')
personajes.sort_by_criterion('name')
personajes.show()

# ====================================================================================#
separador('2) Posicion de The Thing y Rocket Raccoon')
pos_thing = personajes.search('The Thing', 'name')
pos_rocket = personajes.search('Rocket Raccoon', 'name')
print(f'The Thing está en la posición: {pos_thing}')
print(f'Rocket Raccoon está en la posición: {pos_rocket}')

# ====================================================================================#
separador('3) Listado de villanos')
villanos = List()
villanos.add_criterion('name', by_name)
villanos.add_criterion('real_name', by_real_name)
villanos.add_criterion('year', by_year)
for p in personajes:
    if p.is_villain:
        villanos.append(p)
villanos.show()
print(f'\nTotal de villanos: {villanos.size()}')

# ====================================================================================#
separador('4) Villanos que aparecieron antes de 1980')
cola_villanos = Queue()
for v in villanos:
    cola_villanos.arrive(v)

anteriores_1980 = []
for _ in range(cola_villanos.size()):
    villano_actual = cola_villanos.on_front()
    if villano_actual.year < 1980:
        anteriores_1980.append(villano_actual)
    cola_villanos.move_to_end()

for v in anteriores_1980:
    print(v)
print(f'\nTotal de villanos anteriores a 1980: {len(anteriores_1980)}')

# ====================================================================================#
separador('5) Superheroes que comienzan con Bl, G, My, W')
heroes = List()
heroes.add_criterion('name', by_name)
heroes.add_criterion('real_name', by_real_name)
heroes.add_criterion('year', by_year)
for p in personajes:
    if not p.is_villain:
        heroes.append(p)

heroes.filter_start_with(('Bl', 'G', 'My', 'W'))

# ====================================================================================#
separador('6) Listado ascendente por nombre real')
personajes.sort_by_criterion('real_name')
personajes.show()

# ====================================================================================#
separador('7) Superheroes ordenados por fecha de aparición')
heroes.sort_by_criterion('year')
heroes.show()

# ====================================================================================#
separador('8) Modificar nombre real de Ant Man')
pos_antman = personajes.search('Ant Man', 'name')
if pos_antman is not None:
    print(f'Antes: {personajes[pos_antman]}')
    personajes[pos_antman].real_name = 'Scott Lang'
    print(f'Después: {personajes[pos_antman]}')
else:
    print('Ant Man no está en la lista')

# ====================================================================================#
separador('9) Personajes con "time-traveling" o "suit" en la biografía')
personajes.filter_contain_on_bio(['time-traveling', 'suit'])
# ====================================================================================#
separador('10) Eliminar Electro y Baron Zemo')
eliminado_electro = personajes.delete_value('Electro', 'name')
print(f'Eliminado: {eliminado_electro if eliminado_electro is None else str(eliminado_electro)}')

eliminado_zemo = personajes.delete_value('Baron Zemo', 'name')
print(f'Eliminado: {eliminado_zemo if eliminado_zemo is None else str(eliminado_zemo)}')

print(f'\nTotal de personajes luego de eliminar: {personajes.size()}')
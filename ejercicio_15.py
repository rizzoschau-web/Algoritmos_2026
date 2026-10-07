from list_ import List

entrenadores_data = [
    {"nombre": "Ash Ketchum", "torneos": 5, "perdidas": 25, "ganadas": 75, "pokemons": [
        ("Pikachu", 50, "Electrico", None), ("Charizard", 60, "Fuego", "Volador"),
        ("Greninja", 55, "Agua", "Siniestro"), ("Snorlax", 48, "Normal", None),
        ("Pikachu", 35, "Electrico", None)]},
    {"nombre": "Misty", "torneos": 2, "perdidas": 10, "ganadas": 40, "pokemons": [
        ("Starmie", 45, "Agua", "Psiquico"), ("Gyarados", 52, "Agua", "Volador"),
        ("Psyduck", 30, "Agua", None), ("Wingull", 22, "Agua", "Volador")]},
    {"nombre": "Brock", "torneos": 3, "perdidas": 15, "ganadas": 35, "pokemons": [
        ("Onix", 40, "Roca", "Tierra"), ("Steelix", 54, "Acero", "Tierra"),
        ("Tyrantrum", 58, "Roca", "Dragon"), ("Geodude", 20, "Roca", "Tierra")]},
    {"nombre": "Gary Oak", "torneos": 7, "perdidas": 12, "ganadas": 88, "pokemons": [
        ("Blastoise", 62, "Agua", None), ("Arcanine", 58, "Fuego", None),
        ("Scovillain", 55, "Planta", "Fuego"), ("Terrakion", 70, "Roca", "Lucha"),
        ("Eevee", 30, "Normal", None)]},
    {"nombre": "Cynthia", "torneos": 10, "perdidas": 5, "ganadas": 95, "pokemons": [
        ("Garchomp", 78, "Dragon", "Tierra"), ("Lucario", 74, "Lucha", "Acero"),
        ("Spiritomb", 70, "Fantasma", "Siniestro"), ("Roserade", 72, "Planta", "Veneno"),
        ("Milotic", 71, "Agua", None), ("Togekiss", 73, "Hada", "Volador")]},
    {"nombre": "Lance", "torneos": 6, "perdidas": 20, "ganadas": 80, "pokemons": [
        ("Dragonite", 62, "Dragon", "Volador"), ("Gyarados", 58, "Agua", "Volador"),
        ("Aerodactyl", 55, "Roca", "Volador"), ("Dragonite", 50, "Dragon", "Volador")]},
    {"nombre": "Serena", "torneos": 1, "perdidas": 18, "ganadas": 22, "pokemons": [
        ("Braixen", 36, "Fuego", None), ("Pancham", 30, "Lucha", None),
        ("Sylveon", 40, "Hada", None), ("Wingull", 18, "Agua", "Volador")]},
    {"nombre": "Iris", "torneos": 4, "perdidas": 9, "ganadas": 31, "pokemons": [
        ("Haxorus", 58, "Dragon", None), ("Excadrill", 50, "Tierra", "Acero"),
        ("Emolga", 40, "Electrico", "Volador"), ("Hydreigon", 60, "Siniestro", "Dragon")]},
]

class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.name = nombre
        self.level = nivel
        self.type = tipo
        self.subtype = subtipo

    def __str__(self):
        subtipo = self.subtype if self.subtype else '-'
        return f"{self.name} - nivel {self.level} - {self.type}/{subtipo}"


class Trainer:

    def __init__(self, nombre, torneos, perdidas, ganadas):
        self.name = nombre
        self.tournaments = torneos
        self.lost = perdidas
        self.won = ganadas
        self.pokemons = List()          # lista dentro de la lista (lista de listas)

    def win_percentage(self):
        return self.won * 100 / (self.won + self.lost)

    def __str__(self):
        return self.name

    def info(self):
        return (f"Entrenador: {self.name} | Torneos ganados: {self.tournaments} | "
                f"Batallas ganadas: {self.won} | Batallas perdidas: {self.lost}")


def by_trainer_name(item):
    return item.name

def by_tournaments(item):
    return item.tournaments

def by_pokemon_name(item):
    return item.name

def by_level(item):
    return item.level


list_trainers = List()
list_trainers.add_criterion('trainer_name', by_trainer_name)
list_trainers.add_criterion('tournaments', by_tournaments)
list_trainers.add_criterion('pokemon_name', by_pokemon_name)
list_trainers.add_criterion('level', by_level)

for e in entrenadores_data:
    trainer = Trainer(e['nombre'], e['torneos'], e['perdidas'], e['ganadas'])
    for nombre, nivel, tipo, subtipo in e['pokemons']:
        trainer.pokemons.append(Pokemon(nombre, nivel, tipo, subtipo))
    list_trainers.append(trainer)


def buscar_entrenador(nombre):
    pos = list_trainers.search(nombre, 'trainer_name')
    return list_trainers[pos] if pos is not None else None


def buscar_pokemon(trainer, nombre):
    pos = trainer.pokemons.search(nombre, 'pokemon_name')
    return trainer.pokemons[pos] if pos is not None else None


def cantidad_pokemons(nombre_entrenador):                       # a
    trainer = buscar_entrenador(nombre_entrenador)
    return trainer.pokemons.size() if trainer else None


def entrenadores_mas_de_tres_torneos():                         # b
    for trainer in list_trainers:
        if trainer.tournaments > 3:
            print(f'{trainer.name} ({trainer.tournaments} torneos)')


def pokemon_mayor_nivel_del_mas_ganador():                      # c
    list_trainers.sort_by_criterion('tournaments')
    mejor = list_trainers[-1]                                   # el último es el de más torneos
    mejor.pokemons.sort_by_criterion('level')
    return mejor, mejor.pokemons[-1]


def mostrar_entrenador(nombre_entrenador):                      # d
    trainer = buscar_entrenador(nombre_entrenador)
    if trainer is None:
        print('entrenador no encontrado')
        return
    print(trainer.info())
    print('Pokemons:')
    trainer.pokemons.show()


def entrenadores_porcentaje_mayor(minimo):                      # e
    for trainer in list_trainers:
        if trainer.win_percentage() > minimo:
            print(f'{trainer.name}: {trainer.win_percentage():.1f}%')


def tiene_tipos(pokemon, tipo_a, tipo_b):
    return {pokemon.type, pokemon.subtype} == {tipo_a, tipo_b}


def entrenadores_por_tipos():                                   # f
    for trainer in list_trainers:
        for p in trainer.pokemons:
            if tiene_tipos(p, 'Fuego', 'Planta') or tiene_tipos(p, 'Agua', 'Volador'):
                print(f'{trainer.name}: {p}')


def promedio_nivel(nombre_entrenador):                          # g
    trainer = buscar_entrenador(nombre_entrenador)
    if trainer is None or trainer.pokemons.size() == 0:
        return None
    total = sum(p.level for p in trainer.pokemons)
    return total / trainer.pokemons.size()


def cuantos_tienen_pokemon(nombre_pokemon):                     # h
    cantidad = 0
    for trainer in list_trainers:
        if trainer.pokemons.search(nombre_pokemon, 'pokemon_name') is not None:
            cantidad += 1
    return cantidad


def entrenadores_con_repetidos():                               # i
    for trainer in list_trainers:
        trainer.pokemons.sort_by_criterion('pokemon_name')
        repetidos = set()
        for i in range(1, trainer.pokemons.size()):
            if trainer.pokemons[i].name == trainer.pokemons[i - 1].name:
                repetidos.add(trainer.pokemons[i].name)
        if repetidos:
            print(f'{trainer.name}: {", ".join(sorted(repetidos))}')


def entrenadores_con_alguno(nombres):                           # j
    for trainer in list_trainers:
        encontrados = [n for n in nombres
                       if trainer.pokemons.search(n, 'pokemon_name') is not None]
        if encontrados:
            print(f'{trainer.name}: {", ".join(encontrados)}')


def entrenador_tiene_pokemon(nombre_entrenador, nombre_pokemon):   # k
    trainer = buscar_entrenador(nombre_entrenador)
    if trainer is None:
        print(f'El entrenador {nombre_entrenador} no existe')
        return
    pokemon = buscar_pokemon(trainer, nombre_pokemon)
    if pokemon is None:
        print(f'{trainer.name} no tiene a {nombre_pokemon}')
    else:
        print(f'{trainer.name} si tiene a {pokemon.name}')
        print(trainer.info())
        print(pokemon)


ENTRENADOR = 'Cynthia'
POKEMON = 'Gyarados'

print(f'a. Cantidad de pokemons de {ENTRENADOR}: {cantidad_pokemons(ENTRENADOR)}')

print('\nb. Entrenadores con más de 3 torneos ganados')
entrenadores_mas_de_tres_torneos()

print('\nc. Pokemon de mayor nivel del entrenador con más torneos')
mejor, pokemon = pokemon_mayor_nivel_del_mas_ganador()
print(f'{mejor.name} ({mejor.tournaments} torneos) -> {pokemon}')

print(f'\nd. Datos de {ENTRENADOR} y sus pokemons')
mostrar_entrenador(ENTRENADOR)

print('\ne. Entrenadores con más de 79% de batallas ganadas')
entrenadores_porcentaje_mayor(79)

print('\nf. Entrenadores con pokemons fuego/planta o agua/volador')
entrenadores_por_tipos()

print(f'\ng. Promedio de nivel de los pokemons de {ENTRENADOR}: {promedio_nivel(ENTRENADOR):.2f}')

print(f'\nh. Entrenadores que tienen a {POKEMON}: {cuantos_tienen_pokemon(POKEMON)}')

print('\ni. Entrenadores con pokemons repetidos')
entrenadores_con_repetidos()

print('\nj. Entrenadores con Tyrantrum, Terrakion o Wingull')
entrenadores_con_alguno(['Tyrantrum', 'Terrakion', 'Wingull'])

print('\nk. ¿El entrenador X tiene al pokemon Y?')
x = input('Nombre del entrenador: ').strip().title()
y = input('Nombre del pokemon: ').strip().title()
entrenador_tiene_pokemon(x, y)

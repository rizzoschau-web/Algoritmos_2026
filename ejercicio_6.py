from list_ import List


superheroes = [
    {"nombre": "Spider-Man", "anio_aparicion": 1962, "casa": "Marvel",
     "biografia": "Peter Parker fue mordido por una araña radiactiva y obtuvo poderes de superhéroe. Trabaja como fotógrafo freelance mientras protege Nueva York."},
    {"nombre": "Iron Man", "anio_aparicion": 1963, "casa": "Marvel",
     "biografia": "Tony Stark, genio multimillonario e inventor, construyó una armadura tecnológica para escapar de sus captores. Fundador de los Vengadores."},
    {"nombre": "Wolverine", "anio_aparicion": 1974, "casa": "Marvel",
     "biografia": "Logan posee un esqueleto recubierto de adamantium y garras retráctiles. Su factor de curación acelerada lo hace casi inmortal. Miembro icónico de los X-Men."},
    {"nombre": "Thor", "anio_aparicion": 1962, "casa": "Marvel",
     "biografia": "Dios nórdico del trueno e hijo de Odín. Empuña el martillo Mjolnir y defiende tanto Asgard como la Tierra."},
    {"nombre": "Black Widow", "anio_aparicion": 1964, "casa": "Marvel",
     "biografia": "Natasha Romanoff fue entrenada desde niña como espía. Es una agente de élite de S.H.I.E.L.D., experta en artes marciales."},
    {"nombre": "Hulk", "anio_aparicion": 1962, "casa": "Marvel",
     "biografia": "El científico Bruce Banner se transforma en un gigante verde de fuerza descomunal cuando se enfurece."},
    {"nombre": "Captain America", "anio_aparicion": 1941, "casa": "Marvel",
     "biografia": "Steve Rogers fue transformado en supersoldado durante la Segunda Guerra Mundial y empuña un escudo de vibranium."},
    {"nombre": "Black Panther", "anio_aparicion": 1966, "casa": "Marvel",
     "biografia": "T'Challa, rey de Wakanda, usa un traje de vibranium que absorbe energía cinética para proteger a su nación."},
    {"nombre": "Dr. Strange", "anio_aparicion": 1963, "casa": "DC",
     "biografia": "Stephen Strange, ex cirujano, se convirtió en el Hechicero Supremo y protege la Tierra de amenazas místicas."},
    {"nombre": "Capitana Marvel", "anio_aparicion": 1968, "casa": "Marvel",
     "biografia": "Carol Danvers, piloto de la fuerza aérea, obtuvo poderes cósmicos y puede volar y proyectar energía."},
    {"nombre": "Star-Lord", "anio_aparicion": 1976, "casa": "Marvel",
     "biografia": "Peter Quill, mitad humano y mitad alienígena, lidera a los Guardianes de la Galaxia."},
    {"nombre": "Magneto", "anio_aparicion": 1963, "casa": "Marvel",
     "biografia": "Mutante con control total sobre los campos magnéticos, líder de la Hermandad de Mutantes."},
    {"nombre": "Storm", "anio_aparicion": 1975, "casa": "Marvel",
     "biografia": "Ororo Munroe puede controlar el clima. Es una de las líderes de los X-Men."},
    {"nombre": "Batman", "anio_aparicion": 1939, "casa": "DC",
     "biografia": "Bruce Wayne presenció el asesinato de sus padres y juró proteger Gotham. Sin poderes, usa su inteligencia, fortuna y un traje con muchas herramientas."},
    {"nombre": "Superman", "anio_aparicion": 1938, "casa": "DC",
     "biografia": "Kal-El fue enviado desde Krypton antes de su destrucción. Adoptado como Clark Kent en Kansas, usa sus poderes solares para defender la Tierra."},
    {"nombre": "Mujer Maravilla", "anio_aparicion": 1941, "casa": "DC",
     "biografia": "Diana, princesa de las Amazonas de Temyscira, fue criada como guerrera. Porta el lazo de la verdad y brazaletes indestructibles."},
    {"nombre": "Flash", "anio_aparicion": 1956, "casa": "DC",
     "biografia": "Barry Allen era un científico forense que fue alcanzado por un rayo. Obtuvo la capacidad de moverse a velocidades superlumínicas."},
    {"nombre": "Linterna Verde", "anio_aparicion": 1959, "casa": "DC",
     "biografia": "Hal Jordan fue elegido por el anillo de poder de los Guardianes del Universo, que crea construcciones de energía verde."},
    {"nombre": "Aquaman", "anio_aparicion": 1941, "casa": "DC",
     "biografia": "Arthur Curry, rey de Atlantis, puede respirar bajo el agua y comunicarse con la vida marina."},
    {"nombre": "Shazam", "anio_aparicion": 1940, "casa": "DC",
     "biografia": "El joven Billy Batson se transforma en un poderoso héroe al pronunciar una palabra mágica."},
    {"nombre": "Martian Manhunter", "anio_aparicion": 1955, "casa": "DC",
     "biografia": "J'onn J'onzz, último sobreviviente de Marte, posee telepatía, cambio de forma y fuerza sobrehumana."},
    {"nombre": "Cyborg", "anio_aparicion": 1980, "casa": "DC",
     "biografia": "Victor Stone fue reconstruido con tecnología alienígena tras un accidente y es miembro de la Liga de la Justicia."},
]


class Superhero:

    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return self.name

    def info(self):
        return (f"Nombre: {self.name}\nAño de aparición: {self.year}\n"
                f"Casa: {self.house}\nBiografía: {self.bio}")


def by_name(item):
    return item.name

def by_year(item):
    return item.year


list_heroes = List()
list_heroes.add_criterion('name', by_name)
list_heroes.add_criterion('year', by_year)

for hero in superheroes:
    list_heroes.append(
        Superhero(hero['nombre'], hero['anio_aparicion'], hero['casa'], hero['biografia'])
    )


print('a. Eliminar a Linterna Verde')
deleted_value = list_heroes.delete_value('Linterna Verde', 'name')
print(f'valor eliminado: {deleted_value}')

print('\nb. Año de aparición de Wolverine')
wolverine = list_heroes.search('Wolverine', 'name')
if wolverine is not None:
    print(f'El año de aparición de {list_heroes[wolverine].name} es {list_heroes[wolverine].year}')
else:
    print('no esta en la lista')

print('\nc. Cambiar la casa de Dr. Strange a Marvel')
strange = list_heroes.search('Dr. Strange', 'name')
if strange is not None:
    print(f'antes: {list_heroes[strange].house}')
    list_heroes[strange].house = 'Marvel'
    print(f'ahora: {list_heroes[strange].house}')

print('\nd. Biografía con "traje" o "armadura"')
list_heroes.filter_contain_on_bio(['traje', 'armadura'])

print('\ne. Nombre y casa de los anteriores a 1963')
for hero in list_heroes:
    if hero.year < 1963:
        print(f'{hero.name} - {hero.house}')

print('\nf. Casa de Capitana Marvel y Mujer Maravilla')
for nombre in ('Capitana Marvel', 'Mujer Maravilla'):
    pos = list_heroes.search(nombre, 'name')
    if pos is not None:
        print(f'{nombre}: {list_heroes[pos].house}')
    else:
        print(f'{nombre} no esta en la lista')

print('\ng. Toda la información de Flash y Star-Lord')
for nombre in ('Flash', 'Star-Lord'):
    pos = list_heroes.search(nombre, 'name')
    if pos is not None:
        print(list_heroes[pos].info())
        print()
    else:
        print(f'{nombre} no esta en la lista')

print('h. Superhéroes que comienzan con B, M y S')
list_heroes.filter_start_with(('B', 'M', 'S'))

print('\ni. Cantidad de superhéroes por casa')
cantidad = {}
for hero in list_heroes:
    cantidad[hero.house] = cantidad.get(hero.house, 0) + 1
for casa, total in cantidad.items():
    print(f'{casa}: {total}')

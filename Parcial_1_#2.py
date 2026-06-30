# Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:
# Listado ordenado de manera ascendente por nombre de los personajes. LISTO
# Determinar en que posicion esta The Thing y Rocket Raccoon. LISTO
# Listar todos los villanos de la lista. LISTO
# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980. LISTO
# Listar los superheores que comienzan con  Bl, G, My, y W. listo
# Listado de personajes ordenado por nombre real de manera ascendente de los personajes. LISTO
# Listado de superheroes ordenados por fecha de aparación. LISTO
# Modificar el nombre real de Ant Man a Scott Lang. LISTO
# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit. LISTO
# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista. LISTO

from typing import Any
from super_heroes_data import superheroes

# ------------ INICIO COLA -------------
class queue:

    def __init__(self):
        self.__items = []

    def arrive(self, value: Any) -> None:
        self.__items.append(value)
    
    def attention(self) -> Any:
        if not self.is_empty():
            return self.__items.pop(0)
        else:
            print("No hay elementos en la Cola.")

    def size(self) -> int:
        if not self.is_empty():
            return len(self.__items)
        else:
            print("No hay elementos en la Cola.")

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def on_front(self) -> Any:
        if not self.is_empty():
            return self.items[0]
        else:
            print("No hay elementos en la Cola.")

    def move_to_end(self) -> Any:
        value = self.items.pop(0)
        self.items.append(value)
        return value

    def show(self) -> None:
        for i in range(len(self.__items)):
            value = self.items.pop(0)
            return value
# ------------ FIN COLA -------------

def separador():
    print("\n" + "-" * 50 + "\n")

print(" INICIO DEL PROGRAMA ".center(50, "="))

print("Listado ordenado de manera ascendente por nombre de los personajes.")
orden_nombre = sorted(superheroes, key=lambda h:h["name"].lower())
for i, h in enumerate(orden_nombre, 1):
    print(f" {i}. {h['name']}")
separador()
print("Determinar en que posicion esta The Thing y Rocket Raccoon.")
for buscado in ("The Thing", "Rocket Racoon"):
    for i, h in enumerate(orden_nombre, 1):
        if h["name"] == buscado:
            print(f"{buscado}: posición {i}")
            break
    else:
        print(f"'{buscado}' no se encuentra en la lista.")
separador()
print("Listar todos los villanos de la lista.")
villanos = [h for h in superheroes if h["is_villain"]]
for i, v in enumerate(villanos, 1):
    print(f"{i}. {v['name']} ({v['first_appearance']})")
separador()
("Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.")
cola = queue()
for v in villanos:
    cola.arrive(v)

print("Villanos creados antes de 1980: ")
total = cola.size()
for _ in range(total):
    v = cola.attention()
    if v and v["first_appearance"] < 1980:
        print(f"{v['name']} ({v['first_appearance']})")
separador()
print("Listar los superheores que comienzan con  Bl, G, My, y W.")
prefijos = ("Bl", "G", "My", "W")
for h in sorted(superheroes, key=lambda h: h["name"].lower()):
    for p in prefijos:
        if h["name"].startswith(p):
            print(f" [{p}] {h['name']}")
            break
separador()
print("Listado de personajes ordenado por nombre real de manera ascendente de los personajes.")
orden_real = sorted(superheroes, key= lambda h: h["real_name"] or "".lower())
for i, h in enumerate(orden_real, 1):
    print(f"{i}. {h['real_name']} es {h['name']}")
separador()
print("Listado de superheroes ordenados por fecha de aparación.")
char_fecha = sorted(superheroes, key=lambda x: x["first_appearance"])
for personaje in char_fecha: 
    print(personaje["name"], personaje["first_appearance"])  
separador()
print("Modificar el nombre real de Ant Man a Scott Lang.")
for h in superheroes:
    if h["name"] == "Ant Man":
        print(f" Antes: {h['real_name']}")
        h["real_name"] = "Scott Lang"
        print(f"Después: {h['real_name']}")
        break
separador()
print("Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.")
for h in superheroes:
    bio = h["short_bio"].lower()
    if "time-travelling" in bio or "suit" in bio:
        print(f"{h['name']}")
separador()
print("Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.")
elim_char = ["Electro", "Baron Zemo"]

for nombre in elim_char:
    for personaje in superheroes:
        if personaje["name"] == nombre:
            print("Personaje Eliminado: ")
            print(personaje)
            
            superheroes.remove(personaje)
            break

print(" FIN DEL PROGRAMA ".center(50, "="))
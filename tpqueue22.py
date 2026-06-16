from typing import Any

class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Any:
        return self.__elements.pop(0)

    def size(self) -> int:
        return len(self.__elements)

    def on_front(self) -> Any:
        return self.__elements[0]

    def move_to_end(self) -> Any:
        value = self.__elements.pop(0)
        self.__elements.append(value)
        return value

    def show(self) -> None:
        for i in range(len(self.__elements)):
            value = self.move_to_end()
            print(value)


cola = Queue()

cola.arrive(("Tony Stark", "Iron Man", "M"))
cola.arrive(("Steve Rogers", "Capitán América", "M"))
cola.arrive(("Natasha Romanoff", "Black Widow", "F"))
cola.arrive(("Carol Danvers", "Capitana Marvel", "F"))
cola.arrive(("Scott Lang", "Ant-Man", "M"))

cola_aux = Queue()

personaje_capitana_marvel = ""
superheroe_scott = ""
superheroe_carol = ""

superheroes_femeninos = []
personajes_masculinos = []
empiezan_con_s = []

while cola.size() > 0:

    personaje = cola.attention()
    
    if personaje[1] == "Capitana Marvel":
        personaje_capitana_marvel = personaje[0]

    if personaje[2] == "F":
        superheroes_femeninos.append(personaje[1])

    if personaje[2] == "M":
        personajes_masculinos.append(personaje[0])

    if personaje[0] == "Scott Lang":
        superheroe_scott = personaje[1]

    if personaje[0].startswith("S") or personaje[1].startswith("S"):
        empiezan_con_s.append(personaje)

    if personaje[0] == "Carol Danvers":
        superheroe_carol = personaje[1]

    cola_aux.arrive(personaje)

while cola_aux.size() > 0:
    cola.arrive(cola_aux.attention())


print("a) Nombre del personaje de Capitana Marvel:")
print(personaje_capitana_marvel)

print("\nb) Superhéroes femeninos:")
for heroe in superheroes_femeninos:
    print(heroe)

print("\nc) Personajes masculinos:")
for personaje in personajes_masculinos:
    print(personaje)

print("\nd) Superhéroe de Scott Lang:")
print(superheroe_scott)

print("\ne) Datos cuyos nombres comienzan con S:")
for dato in empiezan_con_s:
    print(dato)

print("\nf) Carol Danvers se encuentra en la cola.")
print("Su nombre de superhéroe es:")
print(superheroe_carol)
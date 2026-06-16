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


class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        return self.__elements.pop()

    def size(self) -> Any:
        return len(self.__elements)


cola = Queue()

cola.arrive(("10:30", "Facebook", "Nuevo mensaje"))
cola.arrive(("12:15", "Twitter", "Enseñando Python"))
cola.arrive(("13:40", "Instagram", "Nueva publicacion"))
cola.arrive(("14:20", "Twitter", "Python es genial"))
cola.arrive(("16:10", "Facebook", "Nueva solicitud"))


cola_aux = Queue()

while cola.size() > 0:
    notificacion = cola.attention()

    if notificacion[1] != "Facebook":
        cola_aux.arrive(notificacion)

while cola_aux.size() > 0:
    cola.arrive(cola_aux.attention())


print("Notificaciones de Twitter con Python:")

cola_aux = Queue()

while cola.size() > 0:
    notificacion = cola.attention()

    if notificacion[1] == "Twitter" and "Python" in notificacion[2]:
        print(notificacion)

    cola_aux.arrive(notificacion)

while cola_aux.size() > 0:
    cola.arrive(cola_aux.attention())


pila = Stack()
cola_aux = Queue()

while cola.size() > 0:
    notificacion = cola.attention()

    hora = notificacion[0]

    if "11:43" <= hora <= "15:57":
        pila.push(notificacion)

    cola_aux.arrive(notificacion)

while cola_aux.size() > 0:
    cola.arrive(cola_aux.attention())

print("\nCantidad de notificaciones entre 11:43 y 15:57:")
print(pila.size())
# Ejercicios 5 y 22, Recursividad. Sbir a GitHub y pasar link de la entrega.

# 5. Desarrollar una función que permita convertir un número romano en un número decimal.

def rom_a_dec ( romano: str ) -> int:
    val = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    if len(romano) == 0:
        return 0
    
    if len(romano) >= 2 and val[romano[0]] < val[romano[1]]:
        valor_actual = val[romano[1]] - val[romano[0]]
        return valor_actual + rom_a_dec(romano[2:])
    
print(rom_a_dec("XL"))
print(rom_a_dec("IV"))

# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.

def usar_la_fuerza (mochila: list, index: int = 0) -> tuple: 
    if index >= len(mochila):
        print ("La fuerza no encontró ningun sable de luz.")
        return (False, index)
    
    objeto_act = mochila[index]
    print(f"[{index + 1}] Luke Skywalker saca un: '{objeto_act}'")

    if objeto_act == "Sable de luz":
        print(f"Luke Skywalker saca un Sable de Luz. Objeto encontrado: {index + 1}")
        return (True, index + 1)
    
    return usar_la_fuerza(mochila, index + 1)

# Items sacados de internet porque no conozco de Star Wars. :(
mochila_jedi = ["Cristal kyber de repuesto", "Comunicador holográfico", "Raciones de comida", "Cantimplora de agua", "Botiquín médico", "Túnica extra o capa", "Herramientas de reparación", "Sable de luz", "Datapad", "Créditos galácticos", "Gancho magnético", "Meditador portátil", "Mapa estelar"]

print("Luke utiliza la fuerza para sacar un objeto de su mochila")
encontrado, caantidad = usar_la_fuerza(mochila_jedi)
print(f"{'Sable encontrado.' if encontrado else 'No tienes un Sable.'} Objetos Sacados: {caantidad}")
import random

palabras = ["Arbol", "Camioneta", "Python", "Terraplanismo", "Ubuntu", "Cactus", "Fortnite"]
palabra = palabras[random.randint(0, len(palabras))].upper()
palabra_oculta = "_"*len(palabra)

letras_dichas = []

cantidad_intentos = 6
intentos_realizados = 0

def buscar_en_palabra(letra_usuario: str):
    posiciones_letra = []
    for i in range(len(palabra)):
        if letra_usuario.upper() == palabra[i].upper():
            posiciones_letra.append(i)
    return posiciones_letra

def cambiar_palabra_oculta(lista_posiciones: list, letra: str):
    while lista_posiciones:
        index = lista_posiciones.pop(0)
        palabra_oculta[index] = letra.upper()

while intentos_realizados < cantidad_intentos:
    print(f"La palabra oculta es: {palabra_oculta}")
    letra = input("Ingrese una letra: ").upper()
    if letra in letras_dichas:
        print("Letra ya mencionada")
    else:
        index_letras = buscar_en_palabra(letra)
        cambiar_palabra_oculta(index_letras, letra)
        letras_dichas.append(letra)
    
    if "_" not in palabra_oculta:
        print("Ganaste")
        break
    intentos_realizados += 1

if intentos_realizados == 6:
    print("Limite de intenso superado") 
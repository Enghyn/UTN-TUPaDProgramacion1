import random

numeros_carton = random.sample(range(1, 51), 25)
elección_numeros_aleatorios = random.sample(range(1, 51), 25)

filas = 5
columnas = 5

carton = [[numeros_carton.pop() for _ in range(columnas)] for _ in range(filas)]

print("Cartón de bingo:")
for fila in carton:
    for numero in fila:
        if numero < 10:
            print(numero, end="  ")
        else:
            print(numero, end=" ")
    print()

termino = False # Variable para controlar el fin del juego
index_filas = [] # Lista para almacenar los índices de las filas completadas

while not termino and len(elección_numeros_aleatorios) > 0:
    numero_bingo = elección_numeros_aleatorios.pop()
    termino = True
    elemento_en_fila = False
    contador = 0 # Contador para identificar la fila
    for fila in carton:
        contador += 1
        if numero_bingo in fila:
            fila[fila.index(numero_bingo)] = 0
            elemento_en_fila = True
        index_filas.append(contador if fila.count(0) == 5 and contador not in index_filas else 0)
    if not elemento_en_fila:
        print(f"\nEl número {numero_bingo} no está en el cartón.")
    
    print("\nCartón actualizado:")
    for fila in carton:
        for numero in fila:
            if numero != 0:
                termino = False
            if numero < 10:
                print(numero, end="  ")
            else:
                print(numero, end=" ")
        print()

    for fila in sorted(index_filas):
        if fila is not 0:
            print(f"¡Fila! La fila {fila} ha sido completada.")

if not termino:
    print("\nSe han agotado los números aleatorios. Fin del juego.")
else:
    print("\n¡Bingo! Has completado el cartón.")
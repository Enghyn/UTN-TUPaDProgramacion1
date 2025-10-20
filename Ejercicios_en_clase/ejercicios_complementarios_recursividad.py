# "P" -> pared
# " " -> camino
# "X" -> salida
# "&" -> dragon
# "." -> ya visitado

laberinto = [["P","P","P","X","P"],
             ["P","&","P"," ","P"],
             ["P"," ","P"," ","P"],
             ["P"," "," "," ","P"],
             ["P","P","P","P","P"]]

def buscar_salida(laberinto, fila, columna):
    if laberinto[fila][columna] == "X":
        return True
    elif laberinto[fila][columna] == "P" or laberinto[fila][columna] == ".":
        return False
    elif laberinto[fila][columna] == " " or laberinto[fila][columna] == "&":
        laberinto[fila][columna] = "."
        for fila_lab in laberinto:
            print(fila_lab)
        print("\n")
        print("-----------------------")
        print("\n")
        if buscar_salida(laberinto, fila-1, columna):
            return True
        if buscar_salida(laberinto, fila+1, columna):
            return True
        if buscar_salida(laberinto, fila, columna-1):
            return True
        if buscar_salida(laberinto, fila, columna+1):
            return True

if buscar_salida(laberinto, 1, 1):
    print("Salida")
else:
    print("No se encontro")
import csv

RUTA = "archivo.csv"

def esta_vacio():
    import os
    if os.path.getsize(RUTA) == 0:
        return True
    return False

def iniciar_archivo():
    if esta_vacio():
        with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
            campos = ["nombre", "precio"]
            escritor = csv.writer(archivo)
            escritor.writerow(campos)

def mostrar_producto():
    with open(RUTA, "r", newline="", encoding="UTF-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for linea in lector:
            print(linea)

def agregar_producto(nombre_producto:str, precio_producto:float):
    with open(RUTA, "a", newline="", encoding="UTF-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre_producto, precio_producto])


def buscar_producto(nombre_producto:str):
    with open(RUTA, "r", newline="", encoding="UTF-8") as archivo:
        lector = csv.reader(archivo)
        for linea in lector:
            if linea[0] == nombre_producto:
                return True
        return False

def eliminar_producto(nombre_producto:str):
    with open(RUTA, "r", newline="", encoding="UTF-8") as archivo:
        lector = csv.reader(archivo)
        lineas = [linea for linea in lector if linea[0] != nombre_producto]
    
    with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(lineas)

def actualizar_producto(nombre_producto:str, precio_nuevo:float):
    with open(RUTA, "r", newline="", encoding="UTF-8") as archivo:
        lector = csv.reader(archivo)
        lineas = []
        for linea in lector:
            if linea[0] == nombre_producto:
                linea[1] = precio_nuevo
            lineas.append(linea)
    with open(RUTA, "w", newline="", encoding="UTF-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(lineas)

iniciar_archivo()
while True:
    try:
        print("""
1) Mostrar productos
2) Agregar producto
3) Eliminar producto
4) Actualizar precio
5) Salir""")
        opcion = int(input(">> ").strip())
    except ValueError:
        print("Ingrese un número")
        continue

    match opcion:
        case 1:
            mostrar_producto()

        case 2:
            try:
                nombre_producto = input("Ingrese el nombre del producto: ").strip()
                precio_producto = float(input("Ingrese el precio del producto:  ").strip())
                if precio_producto == 0:
                    raise ValueError
                agregar_producto(nombre_producto, precio_producto)
            
            except ValueError:
                print("Ingrese un valor numérico")
        
        case 3:
            nombre_producto = input("Ingrese el producto a eliminar: ").strip()
            if not buscar_producto(nombre_producto):
                print("Producto no encontrado")
                continue
            eliminar_producto(nombre_producto)

        case 4:
            try:
                nombre_producto = input("Ingrese el producto a actualizar: ").strip()
                if not buscar_producto(nombre_producto):
                    print("Producto no encontrado")
                    continue
                precio_producto = float(input("Ingrese el precio actualizado: ").strip())
                if precio_producto == 0:
                    raise ValueError
                actualizar_producto(nombre_producto, precio_producto)
            
            except ValueError:
                print("Ingrese un valor numérico")

        case 5:
            print("Saliendo...")
            break

        case _:
            print("Ingrese un número dentro del rango de opciónes")


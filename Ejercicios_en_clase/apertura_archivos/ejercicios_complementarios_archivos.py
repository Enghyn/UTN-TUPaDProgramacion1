import csv

RUTA = "archivo.csv"

def esta_vacio():
    import os
    if os.path.getsize(RUTA) == 0:
        return True
    return False

def iniciar_archivo():
    if esta_vacio():
        with open(RUTA, "w", newline="") as archivo:
            campos = ["nombre", "precio"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()

def mostrar_producto():
    iniciar_archivo()
    with open(RUTA, "r", newline="") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for linea in lector:
            print(linea)

def agregar_producto():
    iniciar_archivo()
    with open(RUTA, "a", newline="") as archivo:
        while True:
            try:
                escritor = csv.writer(archivo)
                nombre_producto = input("Ingrese el nombre del producto: ").strip()
                precio_producto = float(input("Ingrese el precio del producto:  ").strip())
                if precio_producto == 0:
                    raise ValueError
                escritor.writerow([nombre_producto, precio_producto])
                break
            except ValueError:
                print("Ingrese un valor numérico")
                continue

def buscar_producto(nombre_producto:str):
    iniciar_archivo()
    with open(RUTA, "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for linea in lector:
            if linea['nombre'] == nombre_producto:
                return False
            return [linea['nombre'], linea['precio']]

def eliminar_producto(nombre_producto:str):
    iniciar_archivo()
    with open(RUTA, "a", newline="") as archivo:
        escritor = csv.DictWriter(archivo)
        
        escritor.writer

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
            agregar_producto()
        case 3:
            producto = input("Ingrese el producto a buscar: ").strip()
            if not buscar_producto(producto):
                print("Producto no encontrado")
                continue


        case 4:
            pass
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Ingrese un número dentro del rango de opciónes")


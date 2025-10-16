##Trabajo Practico - Manejo de archivos
##Estudiante: Enzo Giaquinta

##Actividades
RUTA_ARCHIVO = "./08_manejo_de_archivos/producto.txt"

lista_productos = []

def mostrar_productos():
    with open(RUTA_ARCHIVO, "r", encoding="utf-8", newline="") as archivo:
        for linea in archivo:
            nombre_producto, precio_producto, cantidad_producto = linea.strip().split(",")
            print(f"Producto: {nombre_producto} | Precio: {precio_producto} | Cantidad: {cantidad_producto}")
            lista_productos.append({"nombre": precio_producto, "precio": float(precio_producto), "cantidad": int(cantidad_producto)})

def agregar_producto(nombre_producto:str, precio_producto:float, cantidad_producto:int):
    if buscar_producto(nombre_producto) != False:
        return print("Producto ya existente")
    
    with open(RUTA_ARCHIVO, "a", encoding="utf-8", newline="") as archivo:
        archivo.write(f"{nombre_producto},{precio_producto},{cantidad_producto}\n")

def buscar_producto(nombre_producto:str):
    with open(RUTA_ARCHIVO, "r", encoding="utf-8", newline="") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            if nombre == nombre_producto:
                return (nombre, precio, cantidad)
        return False


print("-- Leyendo datos del archivo --")
mostrar_productos()

print("\n-- Agregar un producto --")

while True:
    try:
        nombre = input("Ingrese en nombre del producto: ").strip()
        precio = float(input("Ingrese el precio del producto: ").strip())
        cantidad = int(input("Ingrese la cantidad de stock del producto: ").strip())
        if not nombre or not precio or not cantidad or precio < 0 or cantidad < 0:
            raise ValueError
        break
    except ValueError:
        print("Error campo vacío o valor negativo. Ingrese los valores correctos")

agregar_producto(nombre, precio, cantidad)

print("\n-- Buscar un producto --")
while True:
    try:
        nombre = input("Ingrese el nombre del producto a buscar: ").strip()
        if not nombre:
            raise ValueError
        break
    except ValueError:
        print("Error de campo vacío. Porfavor ingresar un valor")

producto = buscar_producto(nombre)

if not producto:
    print("Error. Producto no encontrado")
else:
    print(f"Producto: {producto[0]} | Precio: {producto[1]} | Cantidad: {producto[2]}")
##Trabajo Practico - Datos Complejos
##Estudiante: Enzo Giaquinta

##Actividades
#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300
print("Actividad 1")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

print("\n")

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800
print("Actividad 2")

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

print("\n")

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.
print("Actividad 3")

frutas = list(precios_frutas.keys())
print(frutas)

print("\n")

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
print("Actividad 4")

contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    contactos[nombre] = numero

nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
if nombre_buscar in contactos:
    print("El número de", nombre_buscar, "es:", contactos[nombre_buscar])
else:
    print("Contacto no encontrado.")

print("\n")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
print("Actividad 5")

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1
print("Cantidad de veces que aparece cada palabra:", contador_palabras)

print("\n")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
print("Actividad 6")

alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio}")

print("\n")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
print("Actividad 7")

parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {104, 105, 106, 107, 108}

aprobados_ambos = parcial_1.intersection(parcial_2)
print("Aprobados en ambos parciales:", aprobados_ambos)

aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2)
print("Aprobados en solo uno de los parciales:", aprobados_solo_uno)

aprobados_total = parcial_1.union(parcial_2)
print("Aprobados en al menos un parcial:", aprobados_total)

print("\n")

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
print("Actividad 8")

stock_productos = {}
while True:
    print("1. Consultar stock")
    print("2. Agregar unidades")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            print("El stock de", producto, "es:", stock_productos[producto])
        else:
            print("Producto no encontrado.")

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
            stock_productos[producto] += unidades
            print("Stock actualizado.")
        else:
            print("Producto no encontrado.")

    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in stock_productos:
            stock_productos[producto] = 0
            print("Producto agregado.")
        else:
            print("El producto ya existe.")

    elif opcion == "4":
        break

    else:
        print("Opción inválida.")

print("\n")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.
print("Actividad 9")

agenda = {("lunes", "10:00"): "Reunión de equipo",
          ("martes", "14:00"): "Cita con el doctor",}

dia = input("Ingrese el día (lunes, martes, etc.): ")
hora = input("Ingrese la hora (HH:MM): ")

evento = agenda.get((dia, hora), "No hay evento programado.")
print("Evento:", evento)

print("\n")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores.
print("Actividad 10")

paises_capitales = {'Argentina': 'Buenos Aires', 'Uruguay': 'Montevideo', 'Chile': 'Santiago', 'Perú': 'Lima'}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario de capitales a países:", capitales_paises)
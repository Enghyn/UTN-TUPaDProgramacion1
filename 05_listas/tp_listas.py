##Trabajo Practico - Listas
##Estudiante: Enzo Giaquinta

##Actividades
#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.
print("Actividad 1")

multiples_de_4 = list(range(4, 101, 4))
print(multiples_de_4)

print("\n")

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo.
print("Actividad 2")

comida = ["pizza", "helado", "chocolate", "pasta", "frutas"]
print(comida[-2])

print("\n")

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla.
print("Actividad 3")

palabras = []
palabras.append("perro")
palabras.append("gato")
palabras.append("loro")
print(palabras)

print("\n")

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. 
print("Actividad 4")

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)

print("\n")

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
#numeros = [8, 15, 3, 22, 7]
#numeros.remove(max(numeros))
#print(numeros)

print("Actividad 5")

print("El programa crea una lista llamada 'numeros' \ncon cinco valores enteros. Luego, utiliza la función 'max()' \npara encontrar el valor máximo en la lista, que es 22. \nA continuación, utiliza el método 'remove()' para eliminar \nese valor máximo de la lista. Finalmente, imprime la lista \nresultante, que ahora contiene los números [8, 15, 3, 7], \nya que el 22 fue eliminado.")

print("\n")

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.
print("Actividad 6")

numeros_saltos = list(range(10, 31, 5))
print(numeros_saltos[:2])

print("\n")

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.
print("Actividad 7")

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "ferrari"
autos[2] = "lamborghini"
print(autos)

print("\n")

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.
print("Actividad 8")

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

print("\n")

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla
print("Actividad 9")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

print("\n")

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.
print("Actividad 10")

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
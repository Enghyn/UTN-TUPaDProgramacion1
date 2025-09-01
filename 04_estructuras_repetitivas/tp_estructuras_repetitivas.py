##Trabajo Practico - Estructuras Repetitivas
##Estudiante: Enzo Giaquinta

##Actividades
#1-Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("Actividad 1")

for i in range(101):
    print(i)

print("\n")

#2-Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
print("Actividad 2")

numero = input("Ingrese un número entero: ")
cantidad_digitos = len(numero)

print("La cantidad de dígitos es:", cantidad_digitos)

print("\n")

#3-Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
print("Actividad 3")

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

suma = 0
for i in range(valor1 + 1, valor2):
    suma += i

print(f"La suma de los números entre {valor1} y {valor2} es: {suma}")

print("\n")

#4-Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
print("Actividad 4")

suma = 0
while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero == 0:
        break
    suma += numero

print(f"La suma total es: {suma}")

print("\n")

#5-Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("Actividad 5")

import random

numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break

print("\n")

#6-Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
print("Actividad 6")

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

print("\n")

#7-Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
print("Actividad 7")

numero = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(numero + 1):
    suma += i

print(f"La suma de los números entre 0 y {numero} es: {suma}")

print("\n")

#8-Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos.
print("Actividad 8")

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(100):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números negativos: {negativos}")
print(f"Números positivos: {positivos}")

print("\n")

#9-Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores.
print("Actividad 9")

suma = 0
for i in range(100):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / 100
print(f"La media de los números ingresados es: {media}")

print("\n")

#10-Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario.
print("Actividad 10")

numero = input("Ingrese un número entero: ")
numero_invertido = ""

for i in range(len(numero) - 1, -1, -1):
    numero_invertido += numero[i]

print(f"El número invertido es: {numero_invertido}")
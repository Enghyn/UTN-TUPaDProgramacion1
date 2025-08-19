##Trabajo Practico - Estructuras Secuenciales
##Estudiante: Enzo Giaquinta

##Actividades
#1-Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Actividad 1")
print("Hola Mundo!\n")

#2-Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
print("Actividad 2")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!\n")

#3- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
print("Actividad 3")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.\n")

#4-Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
print("Actividad 4")
radio = int(input("Ingrese el radio del círculo: "))
PI = 3.14159
area = PI * radio**2
perimetro = 2 * PI * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}\n")

#5- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
print("Actividad 5")
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos // 3600
print(f"{segundos} segundos equivalen a {horas} horas.\n")

#6-Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
print("Actividad 6")
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}\n")

#7-Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("Actividad 7")
print("Ingrese dos numeros enteros distintos de 0")
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
print(f"La suma de {numero1} + {numero2} es: {numero1 + numero2}")
print(f"La resta de {numero1} - {numero2} es: {numero1 - numero2}")
print(f"La multiplicacion de {numero1} * {numero2} es: {numero1 * numero2}")
print(f"La division de {numero1} / {numero2} es: {numero1 / numero2}\n")

#8-Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#IMC = peso en kg / (altura en m)**2
print("Actividad 8")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
IMC = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {IMC}\n")

#9-Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
print("Actividad 9")
temperatura_celsius = float(input("Ingrese una temperatura en grados Celsius: "))
temperatura_fahrenheit = (9/5) * temperatura_celsius + 32
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}\n")

#10-Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
print("Actividad 10")
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los tres numeros es: {promedio}")
import random

print("Bienvenido al piedra, papel o tijeras contra la computadora!!")

ganadas_jugador = 0
ganadas_maquina = 0

while True:
    print("""Elija su opción
          1. Piedra
          2. Papel
          3. Tijeras
          4. Salir
          """)
    opcion = int(input(">> "))
    opcion_computadora = random.randint(1, 3)
    if opcion == 4:
        print("Saliendo...")
        break
    elif opcion < 1 or opcion > 4:
        print("Opción inválida. Intente nuevamente.")
        continue
    else:
        if opcion == 1:
            print("Has elegido Piedra")
        elif opcion == 2:
            print("Has elegido Papel")
        elif opcion == 3:
            print("Has elegido Tijeras")

        if opcion_computadora == 1:
            print("La computadora ha elegido Piedra")
        elif opcion_computadora == 2:
            print("La computadora ha elegido Papel")
        elif opcion_computadora == 3:
            print("La computadora ha elegido Tijeras")

        if opcion == opcion_computadora:
            print("¡Es un empate!")
        elif (opcion == 1 and opcion_computadora == 3) or (opcion == 2 and opcion_computadora == 1) or (opcion == 3 and opcion_computadora == 2):
            print("¡Ganaste!")
            ganadas_jugador += 1
        else:
            print("¡Perdiste!")
            ganadas_maquina += 1

    print(f"Partidas ganadas por el jugador: {ganadas_jugador}")
    print(f"Partidas ganadas por la máquina: {ganadas_maquina}")
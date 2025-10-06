while True:
    try:
        espacios_mochila = int(input("Ingrese la cantidad de espaciso de la mochila: ").strip())
        if espacios_mochila <= 0:
            raise ValueError
        break
    except ValueError:
        print("Error: ingrese solo números mayores a 0.")
        

elemento_vacio = "-- vacío --"
mochila = [elemento_vacio for _ in range(espacios_mochila)]

while True:
    print("""
        --- Menú de la Mochila ---
        1. Guardar objeto
        2. Ver mochila
        3. Eliminar objeto
        4. Salir
        """)
    try:
        opcion = int(input(">> ").strip())
        if opcion <= 0:
            raise ValueError
        elif opcion > 4:
            print("Error: el valor debe estar entre las opciones (1-4).")
    except ValueError:
        print("Error: ingrese solo números mayores a 0.")
    
    match opcion:
        case 1:
            while True:
                try:
                    posicion_mochila = int(input(f"Elija la posicion (0-{espacios_mochila - 1 if espacios_mochila > 0 else 0}): ").strip())
                    if posicion_mochila < 0:
                        raise IndexError
                    objeto = input("Objeto a guardar: ").strip()
                    if not posicion_mochila and not objeto:
                        raise ValueError
                    mochila[posicion_mochila] = objeto
                    break

                except ValueError:
                    print("Error: ingrese solo números mayores a 0.")

                except IndexError:
                    print("Error: espacio de la mochila inválido.")
                    
        case 2:
            print("Contenido de la mochila")
            for i in range(len(mochila)):
                print(f"Espacio {i}: {mochila[i]}")

        case 3:
            while True:
                try:
                    posicion_mochila = int(input(f"Elija la posicion (0-{espacios_mochila - 1 if espacios_mochila > 0 else 0}): ").strip())
                    if not posicion_mochila or posicion_mochila < 0:
                        raise ValueError
                    if mochila[posicion_mochila] == elemento_vacio:
                        print("Ese espacio ya estaba vacío")
                        break
                    print(f"Elemento {mochila[posicion_mochila]} será eliminado")
                    mochila[posicion_mochila] = elemento_vacio
                    break

                except ValueError:
                    print("Error: ingrese solo números mayores a 0.")

                except IndexError:
                    print("Error: posición de la mochila inválido.")
                    
        case 4:
            print("Saliendo....")
            break
#Ingreso de datos del día
datos_fecha = input("Ingresar ['Día'(texto), 'Día'(número)/'MM'(número)]: ").lower()
if "," not in datos_fecha or "/" not in datos_fecha:
    print("Se produjo un error. Formato inválido")
    exit()

else:
    dia, datos_int = datos_fecha.split(",")
    DD, MM = map(int, datos_int.strip().split("/"))

#Verificación de fecha válida
if dia != "lunes" and dia != "martes" and dia != "miercoles" and dia != "jueves" and dia != "viernes":
    print("Se produjo un error. Día inválido")
    exit()

elif 1 > MM or MM > 12:
    print("Se produjo un error. mes inválido")
    exit()

elif MM == 1 or MM == 3 or MM == 5 or MM == 7 or MM == 8 or MM == 10 or MM == 12:
    
    if 1 > DD or DD > 31:
        print("Se produjo un error. Día del mes inválido")
        exit()
    
    else:
        print(f"Fecha ingresada de forma correcta: {dia} {DD}/{MM}")

elif MM == 4 or MM == 6 or MM == 9 or MM == 11:
    
    if 1 > DD or DD > 30:
        print("Se produjo un error. Día del mes inválido")
        exit()
    
    else:
        print(f"Fecha ingresada de forma correcta: {dia} {DD}/{MM}")

elif MM == 2:
    
    if 1 > DD or DD > 28:
        print("Se produjo un error. Día del mes inválido")
        exit()
    
    else:
        print(f"Fecha ingresada de forma correcta: {dia} {DD}/{MM}")

#Ejecución según el día
if dia == "lunes" or dia == "martes" or dia == "miercoles":
    hubo_examen = input("¿Hubo examen? (si/no): ").lower()
    
    if hubo_examen != "si":
        print("No hubo examen")
    
    elif hubo_examen == "si":
        alumnos_aprobados = int(input("Cantidad de alumnos aprobados: "))
        alumnos_reprobados = int(input("Cantidad de alumnos reprobados: "))
        
        if alumnos_aprobados < 0 or alumnos_reprobados < 0:
            print("Se produjo un error. Cantidad de alumnos inválida")
            exit()

        total_alumnos = alumnos_aprobados + alumnos_reprobados
        porcentaje_aprobados = (alumnos_aprobados / total_alumnos) * 100
        print(f"Porcentaje de aprobados: {round(porcentaje_aprobados, 2)}%")
    
    else:
        print("Se produjo un error. Respuesta inválida")
        exit()

elif dia == "jueves":
    porcentaje_asistencia = float(input("Porcentaje de asistencia (sin '%'): "))
    
    if 1 > porcentaje_asistencia or porcentaje_asistencia > 100:
        print("Se produjo un error. Porcentaje inválido")
        exit()
    
    elif porcentaje_asistencia >= 50:
        print("Asistió la mayoría")
    
    else:
        print("No asistió la mayoría")

elif (dia == "viernes") and (DD == 1) and (MM == 1 or MM == 7):
    print("Comienzo de un nuevo ciclo")
    cantidad_alumnos = int(input("Cantidad de alumnos: "))
    arancel = int(input("Arancel por alumno: "))

    if cantidad_alumnos < 0 or arancel < 0:
        print("Se produjo un error. Cantidad inválida")
        exit()

    total_recaudado = cantidad_alumnos * arancel
    print(f"Total recaudado: ${total_recaudado}")

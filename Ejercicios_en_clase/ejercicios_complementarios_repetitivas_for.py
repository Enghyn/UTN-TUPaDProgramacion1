letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

corrimiento = int(input("Ingrese la cantidad de lugares que correr: "))
for contador in range(0,6):
    mensaje = input("Ingrese un mensaje en mayúsculas: ").upper()
    mensaje_cifrado = ""
    
    for letra in mensaje:
        if letra not in letras:
            mensaje_cifrado += letra
        else:
            posicion_letra = letras.index(letra)
            mensaje_cifrado += letras[(posicion_letra + corrimiento)%27]

    print(f"Mensaje cifrado: {mensaje_cifrado}")
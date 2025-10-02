def suma(num1: int, num2: int):
    return num1 + num2

def suma_digitos(numero: int):
    suma_digitos = 0
    for digito in str(numero):
        suma_digitos += int(digito)
    return suma_digitos

suma_num = 0
while True:
    numero_usuario = int(input("Ingrese un numero entero: "))
    if numero_usuario == 0:
        break
    print(f"Suma digitos de {numero_usuario}: {suma_digitos(numero_usuario)}")
    suma_num = suma(suma_num, numero_usuario)

print(f"Suma numeros: {suma_num}")
print(f"Suma digitos: {suma_digitos(suma_num)}")
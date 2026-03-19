suma = 0
contador = 0

while suma < 100:
    try:
        numero = int(input("digita un numero: "))
        if numero < 0:
            print("El numero debe ser positivo")
            continue

        suma+= numero
        contador+= 1

        print(f"valor acumulado {suma}")
    except:
        print("No es un numero")

print("Se alcanzo el limite")

print(f"valor acumulado: {suma}, contador: {contador}")
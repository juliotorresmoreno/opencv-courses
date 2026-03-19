"""
Crea una calculadora básica que realice las cuatro operaciones aritméticas fundamentales (suma, resta, multiplicación y división) entre dos números.

Debes solicitar al usuario que introduzca dos números y luego mostrar el resultado de las cuatro operaciones con estos números.

Para cada operación, muestra el resultado con el siguiente formato:

    "La suma de X y Y es: Z"
    "La resta de X y Y es: Z"
    "La multiplicación de X y Y es: Z"
    "La división de X y Y es: Z"

Recuerda manejar el caso especial de división por cero mostrando un mensaje apropiado.

Pista: Utiliza los operadores +, -, *, / y controla la división por cero con una estructura condicional.
"""

if __name__ == "__main__":
    value1 = float(input("Digite el valor 1: "))
    value2 = float(input("Digite el valor 2: "))
    print(f"El resultado de la suma es {value1+value2}")
    print(f"El resultado de la resta es {value1-value2}")
    print(f"El resultado de la multiplicacion es {value1*value2}")
    if value2 != 0:
        print(f"El resultado de la division es {value1/value2}")
    else:
        print("No se puede dividir entre 0")
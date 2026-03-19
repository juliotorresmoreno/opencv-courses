
edad = int(input("Edad: "))

if edad < 0:
    print("Edad no válida")
elif edad <= 12:
    print("Infante")
elif edad <= 17:
    print("Adolescente")
elif edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")
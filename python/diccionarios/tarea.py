contactos = {
    "persona1": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    "persona2": {"nombre": "Juan", "telefono": "987654321", "email": "juan@ejemplo.com"},
    "persona3": {"nombre": "Maria", "telefono": "123456789", "email": "maria@ejemplo.com"},
    "persona4": {"nombre": "Pedro", "telefono": "123456789", "email": "pedro@ejemplo.com"},
    "persona5": {"nombre": "Luisa", "telefono": "123456789", "email": "luisa@ejemplo.com"},
    "persona6": {"nombre": "Carlos", "telefono": "123456789", "email": "carlos@ejemplo.com"},
    "persona7": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    "persona8": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    "persona9": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    "persona10": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
}

print(contactos["persona2"])

contactos["persona11"] = {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"}

contactos["persona1"]["telefono"] = "555555555"

for contacto in contactos:
    print(contacto)


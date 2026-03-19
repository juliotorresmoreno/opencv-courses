def extraer_info(texto: str):
    tmp = texto.split("@")
    if len(tmp) != 2:
        return {}

    usuario = tmp[0]
    tmp = tmp[1].split(".")

    if len(tmp) < 2:
        return {}

    dominio = ".".join(tmp[0:-1])
    extension = tmp[-1]

    return {
        "nombre_usuario": usuario,
        "dominio": dominio,
        "extension": extension
    }

print(extraer_info("usuario"))
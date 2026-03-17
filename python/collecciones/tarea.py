from collections import Counter

def analizar_texto(value: str):
    sin_espacios = value.replace(" ", "")
    counter = Counter(sin_espacios)
    common = counter.most_common(3)

    return {
        "caracteres_mas_comunes": common,
        "total_caracteres": len(value),
        "total_sin_espacios": len(sin_espacios)
    }

resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
print(resultado)
if 0:
    print("asdas")

import os

def ingresar_calificaciones() -> tuple[list[str], list[float]]:
    materias = []
    calificaciones = []

    if os.environ.get("ENV") == "development":
        materias = [
            "Calculo",
            "Fisica",
            "Programacion",
            "Bases de datos",
            "Ingles"
        ]
        calificaciones = [9.0, 8.0, 7.0, 6.0, 4.5]
        return materias, calificaciones
    
    while True:
        materia = input("Ingrese el nombre de la materia: ")
        calificacion = float(input("Ingrese la calificación: "))

        if materia.strip() == "":
            print("Debe especificar una materia")
            continue

        if calificacion < 0 or calificacion > 10:
            print("La calificación debe estar entre 0 y 10")
            continue

        materias.append(materia)
        calificaciones.append(calificacion)

        continuar = input("¿Desea ingresar otra materia? (s/n): ")
        if continuar == "n":
            break

    return materias, calificaciones

def calcular_promedio(calificaciones: list[float]) -> float:
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral: float = 5):
    estados = []
    for calificacion in calificaciones:
        if calificacion >= umbral:
            estados.append("Aprobado")
        else:
            estados.append("Reprobado")

    return estados

def encontrar_extremos(calificaciones):
    return max(calificaciones), min(calificaciones)

def formatear(datos):
    fields = []
    max_lengths = []
    for field in datos:
        fields.append(field)
        max_length = max([
            len(str(value))
            for value in datos[field]
        ])
        max_lengths.append(max(max_length, len(field)))
    
    row = []
    for j in range(len(fields)):
        padding = (max_lengths[j] - len(fields[j])) * " "
        row.append(fields[j] + padding)

    result = "   ".join(row) + "\n"
    for i in range(len(datos[fields[0]])):
        row = []
        for j in range(len(fields)):
            field = fields[j]
            value = str(datos[field][i])
            padding = (max_lengths[j] - len(value)) * " "
            row.append(value + padding)
        result+= "   ".join(row) + "\n"

    return result

if __name__ == "__main__":
    materias, calificaciones = ingresar_calificaciones()
    promedio_general = calcular_promedio(calificaciones)
    estado_materias = determinar_estado(calificaciones)
    calificacion_maxima, calificacion_minima = encontrar_extremos(calificaciones)
    materia_calificacion_maxima = materias[calificaciones.index(calificacion_maxima)]
    materia_calificacion_minima = materias[calificaciones.index(calificacion_minima)]

    materias_calificaciones = formatear({
        "Materia": materias,
        "Calificacion": calificaciones
    })
    estado_materias = formatear({
        "Materia": materias,
        "Calificacion": calificaciones,
        "Estado": estado_materias
    })

    print("Resumen de resultado")
    print("")
    print("Calificaciones")
    print(materias_calificaciones)
    print("")
    print("Promedio de resultados")
    print(promedio_general)
    print("")

    print("Estado de materias")
    print(estado_materias)
    print("")

    print("Materia mejor calificacion: " + materia_calificacion_maxima + " con " + str(calificacion_maxima))
    print("Materia peor calificacion: " + materia_calificacion_minima + " con " + str(calificacion_minima))

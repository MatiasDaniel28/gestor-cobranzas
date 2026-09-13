

def buscar_consultas(consultas, nombre):
    resultados = []

    for consulta in consultas:
        if consulta["cliente"].casefold() == nombre.strip().casefold():
            resultados.append(consulta)

    return resultados

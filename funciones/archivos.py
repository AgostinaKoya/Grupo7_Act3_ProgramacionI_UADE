from funciones.constantes import CODIGO, COD_PELICULA

# Lectura y escritura de los archivos de texto (no importa otros módulos)

def buscar_pelicula(ruta_peliculas, codigo):
    pelicula = []
    with open(ruta_peliculas, "r", encoding="UTF-8") as archivo:
        encontrado = False
        linea = archivo.readline()
        while linea != "" and not encontrado:
            datos = linea.strip().split(";")
            if datos[CODIGO] == codigo:
                encontrado = True
                pelicula = datos
            else:
                linea = archivo.readline()
    return pelicula


def contar_visualizaciones(ruta_visualizaciones, codigo):
    """Recorre todo el archivo y cuenta las líneas de esa película"""
    cantidad = 0
    with open(ruta_visualizaciones, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")
            if int(datos[COD_PELICULA]) == codigo:
                cantidad += 1
    return cantidad


def minutos_acumulados(ruta_visualizaciones, codigo):
    """Recorre todo el archivo y suma los minutos de esa película"""
    total = 0
    with open(ruta_visualizaciones, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")
            if int(datos[COD_PELICULA]) == codigo:
                total += int(datos[MINUTOS])
    return total



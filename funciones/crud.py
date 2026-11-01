import os
from funciones.constantes import CODIGO, COD_PELICULA, RUTA_TEMP_PELICULAS, RUTA_TEMP_VISUALIZACIONES


def alta_pelicula(ruta_peliculas, codigo, titulo, genero, duracion, calificacion):
    """Agrega una película al final de peliculas.txt"""
    with open(ruta_peliculas, "a", encoding="UTF-8") as archivo:
        archivo.write(f"{codigo};{titulo};{genero};{duracion};{calificacion}\n")        


def modificar_pelicula(ruta_peliculas, codigo, titulo, genero, duracion, calificacion):
    """Reescribe peliculas.txt con los nuevos datos de la película indicada usando un archivo temporal."""
    with open(ruta_peliculas, "r", encoding="UTF-8") as original, \
         open(RUTA_TEMP_PELICULAS, "w", encoding="UTF-8") as temporal:
        for linea in original:
            datos = linea.strip().split(";")
            if int(datos[CODIGO]) == codigo:
                temporal.write(f"{codigo};{titulo};{genero};{duracion};{calificacion}\n")
            else:
                temporal.write(linea)
    os.replace(RUTA_TEMP_PELICULAS, ruta_peliculas)


def baja_en_cascada(ruta_peliculas, ruta_visualizaciones, codigo):
    """Elimina la película de peliculas.txt y todas sus visualizaciones de visualizaciones.txt."""
    with open(ruta_peliculas, "r", encoding="UTF-8") as original, \
         open(RUTA_TEMP_PELICULAS, "w", encoding="UTF-8") as temporal:
        for linea in original:
            datos = linea.strip().split(";")
            if int(datos[CODIGO]) != codigo:
                temporal.write(linea)
    with open(ruta_visualizaciones, "r", encoding="UTF-8") as original, \
         open(RUTA_TEMP_VISUALIZACIONES, "w", encoding="UTF-8") as temporal:
        for linea in original:
            datos = linea.strip().split(";")
            if int(datos[COD_PELICULA]) != codigo:
                temporal.write(linea)
    os.replace(RUTA_TEMP_PELICULAS, ruta_peliculas)
    os.replace(RUTA_TEMP_VISUALIZACIONES, ruta_visualizaciones)
    

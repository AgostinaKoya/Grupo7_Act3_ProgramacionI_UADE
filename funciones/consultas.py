# Listados y consultas que recorren los archivos y muestran cada línea con presentacion.py
from funciones.constantes import COD_PELICULA, MINUTOS
from funciones.archivos import buscar_pelicula
from funciones.presentacion import mostrar_encabezado_peliculas, mostrar_pelicula_fila
from funciones.presentacion import mostrar_encabezado_cruzado, mostrar_fila_cruzado
from funciones.presentacion import mostrar_encabezado_operaciones, mostrar_fila_operacion


def listar_peliculas(ruta_peliculas):
    """Recorre peliculas.txt y muestra todas las películas en una tabla."""
    with open(ruta_peliculas, "r", encoding="UTF-8") as archivo:
        mostrar_encabezado_peliculas()
        for linea in archivo:
            pelicula = linea.strip().split(";")
            mostrar_pelicula_fila(pelicula)


def listar_cruzado(ruta_peliculas, ruta_visualizaciones):
    """Muestra cada visualización con título, género y duración de su película (relación por código)."""
    with open(ruta_visualizaciones, "r", encoding="UTF-8") as archivo:
        mostrar_encabezado_cruzado()
        for linea in archivo:
            visualizacion = linea.strip().split(";")
            pelicula = buscar_pelicula(ruta_peliculas, int(visualizacion[COD_PELICULA]))
            if len(pelicula) > 0:
                mostrar_fila_cruzado(visualizacion, pelicula)


def mostrar_operaciones(ruta_visualizaciones, codigo):
    """Muestra las visualizaciones de una película; devuelve la cantidad y los minutos acumulados."""
    cantidad = 0
    minutos = 0
    mostrar_encabezado_operaciones()
    with open(ruta_visualizaciones, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            visualizacion = linea.strip().split(";")
            if int(visualizacion[COD_PELICULA]) == codigo:
                mostrar_fila_operacion(visualizacion)
                cantidad += 1
                minutos += int(visualizacion[MINUTOS])
    return cantidad, minutos




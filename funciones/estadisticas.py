# Las cuatro estadísticas requeridas
from funciones.constantes import CODIGO
from funciones.consultas import contar_visualizaciones
from funciones.presentacion import mostrar_fila_conteo, mostrar_fila_mas_vista



def total_visualizaciones(ruta_visualizaciones):
    """Estadística 1: devuelve la cantidad total de visualizaciones registradas."""
    total = 0
    with open(ruta_visualizaciones, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            total += 1
    return total


def mostrar_visualizaciones_por_pelicula(ruta_peliculas, ruta_visualizaciones):
    """Estadística 2: devuelve la cantidad de visualizaciones de cada película, incluidas las que tienen 0."""
    with open(ruta_peliculas, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            pelicula = linea.strip().split(";")
            cantidad = contar_visualizaciones(ruta_visualizaciones, int(pelicula[CODIGO]))
            mostrar_fila_conteo(pelicula, cantidad)

def maximo_visualizaciones(ruta_peliculas, ruta_visualizaciones):
    """Estadística 3 (primera pasada): devuelve la mayor cantidad de visualizaciones de una película."""
    maximo = 0
    with open(ruta_peliculas, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            pelicula = linea.strip().split(";")
            cantidad = contar_visualizaciones(ruta_visualizaciones, int(pelicula[CODIGO]))
            if cantidad > maximo:
                maximo = cantidad
    return maximo

def mostrar_mas_visualizadas(ruta_peliculas, ruta_visualizaciones, maximo):
    """Estadística 3 (segunda pasada): muestra todas las películas que alcanzan el máximo (empates incluidos)."""
    with open(ruta_peliculas, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            pelicula = linea.strip().split(";")
            cantidad = contar_visualizaciones(ruta_visualizaciones, int(pelicula[CODIGO]))
            if cantidad == maximo:
                mostrar_fila_mas_vista(pelicula, cantidad)


def promedio_minutos(minutos, cantidad):
    """Estadística 4: devuelve minutos / cantidad, o 0 si la película no tiene visualizaciones."""
    try:
        promedio = minutos / cantidad
    except ZeroDivisionError:
        promedio = 0
    return promedio
        

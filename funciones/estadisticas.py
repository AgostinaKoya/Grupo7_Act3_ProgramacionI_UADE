# Las cuatro estadísticas requeridas
from funciones.constantes import CODIGO, TITULO, COD_PELICULA, MINUTOS
from funciones.consultas import contar_visualizaciones, minutos_acumulados


def total_visualizaciones(visualizaciones):
    """Estadística 1: devuelve la cantidad total de visualizaciones registradas."""
    pass


def visualizaciones_por_pelicula(peliculas, visualizaciones):
    """Estadística 2: devuelve la cantidad de visualizaciones de cada película, incluidas las que tienen 0."""
    pass


def peliculas_mas_visualizadas(peliculas, visualizaciones):
    """Estadística 3: devuelve las películas con más visualizaciones (todas las empatadas) y ese máximo."""
    pass


def promedio_minutos(visualizaciones, codigo):
    """Estadística 4: devuelve el promedio de minutos vistos de una película; sin visualizaciones no divide por cero."""
    pass

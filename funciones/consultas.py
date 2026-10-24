# Búsquedas y cruce de datos sobre las matrices
from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION
from funciones.constantes import NRO_VISUALIZACION, COD_PELICULA, MINUTOS


def buscar_pelicula(peliculas, codigo):
    """Busca una película por código y devuelve su posición en la matriz o -1 si no existe."""
    pass


def visualizaciones_de_pelicula(visualizaciones, codigo):
    """Devuelve la lista de visualizaciones asociadas a un código de película."""
    pass


def contar_visualizaciones(visualizaciones, codigo):
    """Devuelve la cantidad de visualizaciones de una película (0 si no tiene)."""
    pass


def minutos_acumulados(visualizaciones, codigo):
    """Devuelve la suma de minutos vistos de una película (0 si no tiene)."""
    pass


def cruzar_visualizaciones(peliculas, visualizaciones):
    """Devuelve una matriz con cada visualización más título, género y duración de su película."""
    pass

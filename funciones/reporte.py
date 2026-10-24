# Generación del informe consolidado
from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION
from funciones.constantes import NRO_VISUALIZACION, MINUTOS
from funciones.consultas import visualizaciones_de_pelicula, contar_visualizaciones, minutos_acumulados
from funciones.estadisticas import total_visualizaciones, peliculas_mas_visualizadas


def armar_bloque_pelicula(pelicula, operaciones):
    """Devuelve el texto del bloque de una película (datos, visualizaciones, cantidad y minutos)."""
    pass


def armar_resumen_general(peliculas, visualizaciones):
    """Devuelve el texto del resumen final (películas, operaciones, minutos y más visualizadas)."""
    pass


def generar_reporte(ruta, peliculas, visualizaciones):
    """Escribe reporte_visualizaciones.txt (sobrescribe) con todas las películas y el resumen; devuelve True si pudo."""
    pass

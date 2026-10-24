# Lógica de alta, modificación y baja sobre las matrices (no pide datos ni imprime)
from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION, COD_PELICULA
from funciones.consultas import buscar_pelicula


def alta_pelicula(peliculas, codigo, titulo, genero, duracion, calificacion):
    """Agrega la película a la matriz si el código no existe; devuelve True si la agregó, False si estaba repetido."""
    pass


def modificar_pelicula(peliculas, posicion, titulo, genero, duracion, calificacion):
    """Actualiza los campos de la película en esa posición (el código no cambia)."""
    pass


def baja_en_cascada(peliculas, visualizaciones, codigo):
    """Elimina la película y todas sus visualizaciones; devuelve las dos matrices actualizadas."""
    pass

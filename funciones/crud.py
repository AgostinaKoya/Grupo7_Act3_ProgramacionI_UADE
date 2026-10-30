# Lógica de alta, modificación y baja sobre las matrices (no pide datos ni imprime)
from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION, COD_PELICULA
from funciones.consultas import buscar_pelicula


def alta_pelicula(peliculas, codigo, titulo, genero, duracion, calificacion):
    """Agrega la película a la matriz si el código no existe; devuelve True si la agregó, False si estaba repetido."""

    print(peliculas, codigo)
    pos = buscar_pelicula(peliculas, codigo)

    if pos != -1:
        return True

    return False
        


def modificar_pelicula(peliculas, posicion, titulo, genero, duracion, calificacion):

    peliculas[posicion][TITULO] = titulo
    peliculas[posicion][GENERO] = genero
    peliculas[posicion][DURACION] = duracion
    peliculas[posicion][CALIFICACION] = calificacion

    print(peliculas)


def baja_en_cascada(peliculas, visualizaciones, codigo):
    """Elimina la película y todas sus visualizaciones; devuelve las dos matrices actualizadas."""
    nueva_lista_peliculas = []
    nueva_lista_visualizaciones = []


    for pelicula in peliculas:
        if pelicula[CODIGO] != codigo:
            nueva_lista_peliculas.append(pelicula)
    #print(nueva_lista_peliculas)

    for visualizacion in visualizaciones:
        if visualizacion[COD_PELICULA] != codigo:
            nueva_lista_visualizaciones.append(visualizacion)

    return nueva_lista_peliculas, nueva_lista_visualizaciones
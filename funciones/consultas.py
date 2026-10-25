# Búsquedas y cruce de datos sobre las matrices
from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION
from funciones.constantes import NRO_VISUALIZACION, COD_PELICULA, MINUTOS


def buscar_pelicula(peliculas, codigo):
    """Busca una película por código y devuelve su posición en la matriz o -1 si no existe."""
    encontrado = False
    pos = 0
    while pos < len(peliculas) and not encontrado:
        if peliculas[pos][CODIGO] == codigo:
            encontrado = True
        else:
            pos += 1
    if not encontrado:
        pos = -1
    return pos


def visualizaciones_de_pelicula(visualizaciones, codigo):
    """Devuelve la lista de visualizaciones asociadas a un código de película."""
    lista_visualizaciones = []
    
    for registro in visualizaciones:

        if registro[COD_PELICULA] == codigo:
            nro_visualiacion = registro[NRO_VISUALIZACION]
            nro_pelicula = registro[COD_PELICULA]
            minutos = registro[MINUTOS]
            visualizacion = [nro_visualiacion, nro_pelicula,minutos]
            lista_visualizaciones.append(visualizacion) 


    return lista_visualizaciones


def contar_visualizaciones(visualizaciones, codigo):
    """Devuelve la cantidad de visualizaciones de una película (0 si no tiene)."""
    total_visualizaciones=0
    
    for registro in visualizaciones:

        if registro[COD_PELICULA] == codigo:
            total_visualizaciones = total_visualizaciones + 1

    return total_visualizaciones


def minutos_acumulados(visualizaciones, codigo):
    """Devuelve la suma de minutos vistos de una película (0 si no tiene)."""
    total_visualizaciones=0
    
    for registro in visualizaciones:

        if registro[COD_PELICULA] == codigo:
            total_visualizaciones = total_visualizaciones + registro[MINUTOS]

    return total_visualizaciones


def cruzar_visualizaciones(peliculas, visualizaciones):
    """Devuelve una matriz con cada visualización más título, género y duración de su película."""

    matriz_cruzada = []
    
    for visualizacion in visualizaciones:
        codigo = visualizacion[COD_PELICULA]

        pos = buscar_pelicula(peliculas, codigo)
        if pos!= -1:
            pelicula = peliculas[pos]
            nro_visualizacion = visualizacion[NRO_VISUALIZACION]
            titulo_pelicula = pelicula[TITULO]
            genero = pelicula[GENERO]
            duracion = pelicula[DURACION]
            minutos_acumulados = visualizacion[MINUTOS]

            fila = [nro_visualizacion, minutos_acumulados, titulo_pelicula, genero, duracion]
            matriz_cruzada.append(fila)

    return matriz_cruzada            


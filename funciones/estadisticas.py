# Las cuatro estadísticas requeridas
from funciones.constantes import CODIGO, TITULO, COD_PELICULA, MINUTOS
from funciones.consultas import contar_visualizaciones, minutos_acumulados


def total_visualizaciones(visualizaciones):
    """Estadística 1: devuelve la cantidad total de visualizaciones registradas."""
    total = 0
    for registro in visualizaciones:
        total += 1
    return total


def visualizaciones_por_pelicula(peliculas, visualizaciones):
    """Estadística 2: devuelve la cantidad de visualizaciones de cada película, incluidas las que tienen 0."""
    matriz_visualizaciones = []

    for pelicula in peliculas:
        visualizaciones_pelicula = []
        total_pelicula = 0

        for registro in visualizaciones:
            if registro[COD_PELICULA] == pelicula[CODIGO]:
                total_pelicula += 1
                visualizaciones_pelicula.append(registro[COD_PELICULA])
                visualizaciones_pelicula.append(total_pelicula)

        matriz_visualizaciones.append(visualizaciones_pelicula)

    return matriz_visualizaciones


def peliculas_mas_visualizadas(peliculas, visualizaciones):
    """Estadística 3: devuelve las películas con más visualizaciones (todas las empatadas) y ese máximo."""
    
    lista_visualizaciones = visualizaciones_por_pelicula(peliculas, visualizaciones)
    maximo = 0

    for linea in lista_visualizaciones:
        if linea[1] > maximo:
            maximo = linea[1]

    lista_peliculas_mas_visualizadas = []

    for linea in lista_visualizaciones:
        if linea[1] == maximo:
            lista_peliculas_mas_visualizadas.append(linea[CODIGO])
    
    return lista_peliculas_mas_visualizadas, maximo


def promedio_minutos(visualizaciones, codigo):
    """Estadística 4: devuelve el promedio de minutos vistos de una película; sin visualizaciones no divide por cero."""
    pass

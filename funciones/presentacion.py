# Salidas por consola con formato de tabla (solo imprime, no calcula)
from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION
from funciones.constantes import NRO_VISUALIZACION, COD_PELICULA, MINUTOS


def mostrar_peliculas(peliculas):
    """Imprime la tabla de películas con encabezados y columnas alineadas."""
    print(f'{"CÓDIGO":<10}{"TÍTULO":<30}{"GÉNERO":<20}{"DURACIÓN":<12}{"CALIFICACIÓN":<15}')
    print("-" * 80)

    for pelicula in peliculas:
        codigo = pelicula[CODIGO]
        titulo = pelicula[TITULO]
        genero = pelicula[GENERO]
        duracion = pelicula[DURACION]
        calificacion = pelicula[CALIFICACION]
        print(f'{codigo:<10}{titulo:<30}{genero:<20}{duracion:<12}{calificacion:<15}')


def mostrar_pelicula(pelicula, peliculas):
    """Imprime los datos de una sola película."""
    print(f'{"CÓDIGO":<10}{"TÍTULO":<30}{"GÉNERO":<20}{"DURACIÓN":<12}{"CALIFICACIÓN":<15}')
    print("-" * 80)
    codigo = peliculas[pelicula][CODIGO]
    titulo = peliculas[pelicula][TITULO]
    genero = peliculas[pelicula][GENERO]
    duracion = peliculas[pelicula][DURACION]
    calificacion = peliculas[pelicula][CALIFICACION]
    print(f'{codigo:<10}{titulo:<30}{genero:<20}{duracion:<12}{calificacion:<15}')


def mostrar_cruzado(cruzado):
    """Imprime la tabla del listado cruzado de visualizaciones y películas."""
    pass


def mostrar_detalle_operaciones(pelicula, operaciones):
    """Imprime los datos de la película, sus visualizaciones, la cantidad y los minutos acumulados."""
    pass


def mostrar_estadisticas(total, por_pelicula, mas_vistas, maximo):
    """Imprime las estadísticas 1, 2 y 3."""
    pass

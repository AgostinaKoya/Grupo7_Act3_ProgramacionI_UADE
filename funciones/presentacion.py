from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION
from funciones.constantes import NRO_VISUALIZACION, COD_PELICULA, MINUTOS





# ¡¡IMPORTANTE!!
# Salidas por consola con formato de tabla (solo imprimen, no calculan)




def mostrar_encabezado_peliculas():
    """Imprime los encabezados del catálogo de películas."""
    print(f'{"CÓDIGO":<10}{"TÍTULO":<30}{"GÉNERO":<20}{"DURACIÓN":<12}{"CALIFICACIÓN":<15}')
    print("-" * 80)

def mostrar_pelicula_fila(pelicula):
    """Imprime datos de una película en una fila."""
    codigo = pelicula[CODIGO]
    titulo = pelicula[TITULO]
    genero = pelicula[GENERO]
    duracion = pelicula[DURACION]
    calificacion = pelicula[CALIFICACION]
    print(f'{codigo:<10}{titulo:<30}{genero:<20}{duracion:<12}{calificacion:<15}')

def mostrar_pelicula(pelicula):
    """Imprime datos de una película, un dato por línea."""
    print(f'\n{"Código:":<15}{pelicula[CODIGO]}')
    print(f'{"Título:":<15}{pelicula[TITULO]}')
    print(f'{"Género:":<15}{pelicula[GENERO]}')
    print(f'{"Duración:":<15}{pelicula[DURACION]}')
    print(f'{"Calificación:":<15}{pelicula[CALIFICACION]}')

def mostrar_encabezado_cruzado():
    """Imprime el encabezado del listado cruzado de visualizaciones."""
    pass

def mostrar_fila_cruzado(visualizacion, pelicula):
    """Imprime una visualización junto con título, género y duración de su película."""
    print(f"{visualizacion[NRO_VISUALIZACION]:<6}{pelicula[CODIGO]:<8}{pelicula[TITULO]:<30}{pelicula[GENERO]:<18}{pelicula[DURACION]:>10}{visualizacion[MINUTOS]:>9}")

def mostrar_encabezado_operaciones():
    """Imprime el encabezado de la tabla de visualizaciones de una película."""
    pass

def mostrar_fila_operacion(visualizacion):
    """Imprime una visualización (número y minutos vistos)."""
    pass

def mostrar_totales_operaciones(cantidad, minutos):
    """Imprime la cantidad de operaciones y los minutos acumulados, o avisa si no hay operaciones."""
    pass

def mostrar_fila_conteo(pelicula, cantidad):
    """Imprime el código, el título y la cantidad de visualizaciones de una película."""
    pass

def mostrar_fila_mas_vista(pelicula, cantidad):
    """Imprime una de las películas más visualizadas."""
    pass
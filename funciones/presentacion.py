from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION

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
    print(f'{"Duración:":<15}{pelicula[DURACION]} minutos')
    print(f'{"Calificación:":<15}{pelicula[CALIFICACION]}')

def mostrar_totales_operaciones(cantidad, minutos):
    """Imprime la cantidad de operaciones y los minutos acumulados, o avisa si no hay operaciones."""
    print("-" * 38)
    if cantidad == 0:
        print("No existen visualizaciones registradas para esta película.")
    print(f"{'Operaciones:':<22}{cantidad}")
    print(f"{'Minutos acumulados:':<22}{minutos}")


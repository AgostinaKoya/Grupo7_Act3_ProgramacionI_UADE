# Listados y consultas que recorren los archivos y muestran cada línea con presentacion.py
from funciones.constantes import COD_PELICULA, MINUTOS, NRO_VISUALIZACION, CODIGO, TITULO, GENERO, DURACION
from funciones.archivos import buscar_pelicula
from funciones.presentacion import mostrar_pelicula_fila, mostrar_encabezado_peliculas
from funciones.presentacion import mostrar_encabezado_cruzado, mostrar_fila_cruzado
from funciones.presentacion import mostrar_encabezado_operaciones, mostrar_fila_operacion


def listar_peliculas(ruta_peliculas):
    """Recorre peliculas.txt y muestra todas las películas en una tabla."""
    with open(ruta_peliculas, "r", encoding="UTF-8") as archivo:
        print(f'{"CÓDIGO":<10}{"TÍTULO":<30}{"GÉNERO":<20}{"DURACIÓN":<12}{"CALIFICACIÓN":<15}')
        print("-" * 80)
        for linea in archivo:
            pelicula = linea.strip().split(";")
            mostrar_pelicula_fila(pelicula)


def listar_cruzado(ruta_peliculas, ruta_visualizaciones):
    """Muestra cada visualización con título, género y duración de su película (relación por código)."""
    with open(ruta_visualizaciones, "r", encoding="UTF-8") as archivo:
        print(f"{'NRO.':<6}{'CODIGO':<8}{'PELICULA':<30}{'GENERO':<18}{'DURACION':>10}{'MINUTOS':>9}")
        print("-" * 81)
        for linea in archivo:
            visualizacion = linea.strip().split(";")
            pelicula = buscar_pelicula(ruta_peliculas, int(visualizacion[COD_PELICULA]))
            if len(pelicula) > 0:
                print(f"{visualizacion[NRO_VISUALIZACION]:<6}{pelicula[CODIGO]:<8}{pelicula[TITULO]:<30}{pelicula[GENERO]:<18}{pelicula[DURACION]:>10}{visualizacion[MINUTOS]:>9}")


def mostrar_operaciones(ruta_visualizaciones, codigo):
    """Muestra las visualizaciones de una película; devuelve la cantidad y los minutos acumulados."""
    cantidad = 0
    minutos = 0
    print(f"\n{'NRO. VISUALIZACION':<22}{'MINUTOS VISTOS':>16}")
    print("-" * 38)
    with open(ruta_visualizaciones, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            visualizacion = linea.strip().split(";")
            if int(visualizacion[COD_PELICULA]) == codigo:
                print(f"{visualizacion[NRO_VISUALIZACION]:<22}{visualizacion[MINUTOS]:>16}")
                cantidad += 1
                minutos += int(visualizacion[MINUTOS])
    return cantidad, minutos




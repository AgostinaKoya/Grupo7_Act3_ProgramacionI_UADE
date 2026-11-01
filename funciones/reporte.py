from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION
from funciones.constantes import NRO_VISUALIZACION, COD_PELICULA, MINUTOS
from funciones.archivos import contar_visualizaciones
from funciones.estadisticas import maximo_visualizaciones


def escribir_bloque_pelicula(reporte, pelicula, ruta_visualizaciones):
    """Escribe el bloque de una película con sus visualizaciones; devuelve la cantidad y los minutos."""
    reporte.write(f"PELICULA: {pelicula[CODIGO]} - {pelicula[TITULO]}\n")
    reporte.write(f"GENERO: {pelicula[GENERO]}\n")
    reporte.write(f"DURACION: {pelicula[DURACION]} minutos | CALIFICACION: {pelicula[CALIFICACION]}\n\n")
    cantidad = 0
    minutos = 0
    with open(ruta_visualizaciones, "r", encoding="UTF-8") as visualizaciones:
        for linea in visualizaciones:
            datos = linea.strip().split(";")
            if int(datos[COD_PELICULA]) == int(pelicula[CODIGO]):
                if cantidad == 0:
                    reporte.write(f"{'VISUALIZACION':<20}{'MINUTOS VISTOS':>16}\n")
                    reporte.write("-" * 63 + "\n")
                reporte.write(f"{datos[NRO_VISUALIZACION]:<20}{datos[MINUTOS]:>16}\n")
                cantidad += 1
                minutos += int(datos[MINUTOS])
    if cantidad == 0:
        reporte.write("Sin visualizaciones registradas.\n")
    reporte.write(f"\nOPERACIONES: {cantidad}\n")
    reporte.write(f"MINUTOS ACUMULADOS: {minutos}\n")
    reporte.write("=" * 63 + "\n\n")
    return cantidad, minutos

def escribir_mas_visualizadas(reporte, ruta_peliculas, ruta_visualizaciones, maximo):
    """Escribe en el reporte todas las películas que alcanzan el máximo de visualizaciones."""
    with open(ruta_peliculas, "r", encoding="UTF-8") as peliculas:
        for linea in peliculas:
            pelicula = linea.strip().split(";")
            cantidad = contar_visualizaciones(ruta_visualizaciones, int(pelicula[CODIGO]))
            if cantidad == maximo:
                reporte.write(f"  {pelicula[CODIGO]} - {pelicula[TITULO]} ({cantidad} visualizaciones)\n")

def generar_reporte(ruta_peliculas, ruta_visualizaciones, ruta_reporte):
    """Genera (sobrescribe) el informe consolidado con un bloque por película y el resumen general."""
    cantidad_peliculas = 0
    total_operaciones = 0
    total_minutos = 0
    with open(ruta_peliculas, "r", encoding="UTF-8") as peliculas, open(ruta_reporte, "w", encoding="UTF-8") as reporte:
        reporte.write("=" * 63 + "\n")
        reporte.write(f"{'INFORME CONSOLIDADO DE VISUALIZACIONES':^63}\n")
        reporte.write("=" * 63 + "\n\n")
        for linea in peliculas:
            pelicula = linea.strip().split(";")
            cantidad, minutos = escribir_bloque_pelicula(reporte, pelicula, ruta_visualizaciones)
            cantidad_peliculas += 1
            total_operaciones += cantidad
            total_minutos += minutos
        maximo = maximo_visualizaciones(ruta_peliculas, ruta_visualizaciones)
        reporte.write("=" * 63 + "\n")
        reporte.write(f"{'RESUMEN GENERAL':^63}\n")
        reporte.write("=" * 63 + "\n")
        reporte.write(f"PELICULAS: {cantidad_peliculas}\n")
        reporte.write(f"VISUALIZACIONES REGISTRADAS: {total_operaciones}\n")
        reporte.write(f"MINUTOS VISTOS ACUMULADOS: {total_minutos}\n")
        reporte.write("PELICULAS MAS VISUALIZADAS:\n")
        if maximo > 0:
            escribir_mas_visualizadas(reporte, ruta_peliculas, ruta_visualizaciones, maximo)
        else:
            reporte.write("  No hay visualizaciones registradas.\n")
        reporte.write("=" * 63 + "\n")


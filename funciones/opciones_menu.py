# Una función por cada opción del menú: pide datos, llama a las demás funciones y muestra resultados
from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION, RUTA_REPORTE
from funciones.archivos import leer_peliculas, leer_visualizaciones, guardar_peliculas, guardar_visualizaciones
from funciones.validaciones import pedir_entero_positivo, pedir_entero_en_rango, pedir_texto_no_vacio, pedir_confirmacion
from funciones.consultas import buscar_pelicula, visualizaciones_de_pelicula, cruzar_visualizaciones
from funciones.consultas import contar_visualizaciones, minutos_acumulados
from funciones.estadisticas import total_visualizaciones, visualizaciones_por_pelicula
from funciones.estadisticas import peliculas_mas_visualizadas, promedio_minutos
from funciones.presentacion import mostrar_peliculas, mostrar_pelicula, mostrar_cruzado
from funciones.presentacion import mostrar_detalle_operaciones, mostrar_estadisticas
from funciones.crud import alta_pelicula, modificar_pelicula, baja_en_cascada
from funciones.reporte import generar_reporte


def opcion_listar(ruta_peliculas):
    """Opción 1: lee peliculas.txt y muestra la tabla de películas."""
    pass


def opcion_consultar(ruta_peliculas):
    """Opción 2: pide un código y muestra la película o informa que no existe."""
    pass


def opcion_alta(ruta_peliculas):
    """Opción 3: pide y valida los campos, rechaza código repetido y guarda en peliculas.txt."""
    pass


def opcion_modificar(ruta_peliculas):
    """Opción 4: pide un código y nuevos valores (Enter conserva el anterior) y guarda los cambios."""
    pass


def opcion_baja(ruta_peliculas, ruta_visualizaciones):
    """Opción 5: muestra la película y sus visualizaciones, pide confirmación y da de baja en cascada."""
    pass


def opcion_listado_cruzado(ruta_peliculas, ruta_visualizaciones):
    """Opción 6: muestra las visualizaciones junto con título, género y duración de cada película."""
    pass


def opcion_consulta_operaciones(ruta_peliculas, ruta_visualizaciones):
    """Opción 7: pide un código y muestra la película, sus visualizaciones, cantidad y minutos acumulados."""
    pass


def opcion_estadisticas(ruta_peliculas, ruta_visualizaciones):
    """Opción 8: muestra las cuatro estadísticas (el promedio es de una película elegida)."""
    pass


def opcion_informe(ruta_peliculas, ruta_visualizaciones):
    """Opción 9: genera reporte_visualizaciones.txt con la información actualizada."""
    pass

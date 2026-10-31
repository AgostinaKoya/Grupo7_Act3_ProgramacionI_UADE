# Una función por opción del menú: pide los datos, llama a las demás funciones y muestra resultados
from funciones.constantes import TITULO, GENERO, DURACION, CALIFICACION
from funciones.constantes import CALIFICACION_MIN, CALIFICACION_MAX, DURACION_MAX
from funciones.validaciones import pedir_entero_positivo, pedir_entero_en_rango, pedir_texto_no_vacio
from funciones.validaciones import pedir_texto_opcional, pedir_entero_opcional, pedir_confirmacion
from funciones.archivos import buscar_pelicula, contar_visualizaciones, minutos_acumulados
from funciones.consultas import listar_peliculas, listar_cruzado, mostrar_operaciones
from funciones.crud import alta_pelicula, modificar_pelicula, baja_en_cascada
from funciones.estadisticas import total_visualizaciones, mostrar_visualizaciones_por_pelicula
from funciones.estadisticas import maximo_visualizaciones, mostrar_mas_visualizadas, promedio_minutos
from funciones.presentacion import mostrar_pelicula, mostrar_totales_operaciones
from funciones.reporte import generar_reporte

def opcion_listar(ruta_peliculas):
    """Opción 1: muestra la tabla con todas las películas."""
    print("\nLISTADO DE PELÍCULAS\n")
    listar_peliculas(ruta_peliculas)


def opcion_consultar(ruta_peliculas):
    """Opción 2: pide un código, busca y muestra la película, o informa que no existe."""
    codigo = pedir_entero_positivo("Ingrese el código de la película: ")
    pelicula = buscar_pelicula(ruta_peliculas, codigo)
    if len(pelicula) > 0:
        mostrar_pelicula(pelicula)
    else:
        print(f"No existe una película con código {codigo}.")



def opcion_alta(ruta_peliculas):
    """Opción 3: pide y valida los campos; rechaza códigos repetidos y agrega la película al archivo."""
    codigo = pedir_entero_positivo("Ingrese el código de la nueva película: ")
    if len(buscar_pelicula(ruta_peliculas, codigo)) > 0:
        print(f"El código {codigo} ya existe. No se registró la película.")
    else:
        titulo = pedir_texto_no_vacio("Ingrese el título: ")
        genero = pedir_texto_no_vacio("Ingrese el género: ")
        duracion = pedir_entero_en_rango(f"Ingrese la duración en minutos (1 a {DURACION_MAX}): ", 1, DURACION_MAX)
        calificacion = pedir_entero_en_rango(
            f"Ingrese la calificación ({CALIFICACION_MIN} a {CALIFICACION_MAX}): ",
            CALIFICACION_MIN,
            CALIFICACION_MAX
        )
        alta_pelicula(ruta_peliculas, codigo, titulo, genero, duracion, calificacion)
        print(f"Película {codigo} registrada correctamente.")
    


def opcion_modificar(ruta_peliculas):
    """Opción 4: modifica todos los campos salvo el código; Enter conserva el valor anterior."""
    pass

def opcion_baja(ruta_peliculas, ruta_visualizaciones):
    """Opción 5: muestra la película y sus visualizaciones, pide confirmación y da de baja en cascada."""
    pass


def opcion_listado_cruzado(ruta_peliculas, ruta_visualizaciones):
    """Opción 6: muestra cada visualización con los datos de su película."""
    pass


def opcion_consulta_operaciones(ruta_peliculas, ruta_visualizaciones):
    """Opción 7: muestra la película, sus visualizaciones, la cantidad y los minutos acumulados."""
    pass


def opcion_estadisticas(ruta_peliculas, ruta_visualizaciones):
    """Opción 8: muestra las cuatro estadísticas (el promedio es de una película elegida)."""
    pass


def opcion_informe(ruta_peliculas, ruta_visualizaciones, ruta_reporte):
    """Opción 9: genera (sobrescribe) el informe consolidado con la información actualizada."""
    pass

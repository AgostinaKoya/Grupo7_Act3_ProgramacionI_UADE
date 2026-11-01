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
    pelicula = buscar_pelicula(ruta_peliculas, codigo)

    if len(pelicula) > 0:
        print(f"El código {codigo} ya existe. No se registró la película.")
    else:
        titulo = pedir_texto_no_vacio("Ingrese el título: ")
        genero = pedir_texto_no_vacio("Ingrese el género: ")
        duracion = pedir_entero_en_rango(f"Ingrese la duración en minutos (1 a {DURACION_MAX}): ", 1, DURACION_MAX)
        calificacion = pedir_entero_en_rango(f"Ingrese la calificación ({CALIFICACION_MIN} a {CALIFICACION_MAX}): ",CALIFICACION_MIN,CALIFICACION_MAX)
        alta_pelicula(ruta_peliculas, codigo, titulo, genero, duracion, calificacion)
        print(f"Película {codigo} registrada correctamente.")
    


def opcion_modificar(ruta_peliculas):
    """Opción 4: modifica todos los campos salvo el código; Enter conserva el valor anterior."""
    codigo = pedir_entero_positivo("Ingrese el código de la película a modificar: ")
    pelicula = buscar_pelicula(ruta_peliculas, codigo)
    if len(pelicula) > 0:
        mostrar_pelicula(pelicula)
        print("\nIngrese los nuevos valores (Enter para conservar el actual):")
        titulo = pedir_texto_opcional("Título", pelicula[TITULO])
        genero = pedir_texto_opcional("Género", pelicula[GENERO])
        duracion = pedir_entero_opcional("Duración", int(pelicula[DURACION]), 1, DURACION_MAX)
        calificacion = pedir_entero_opcional("Calificación", int(pelicula[CALIFICACION]), CALIFICACION_MIN, CALIFICACION_MAX)
        modificar_pelicula(ruta_peliculas, codigo, titulo, genero, duracion, calificacion)
        print(f"Película {codigo} modificada correctamente.")
    else:
        print(f"No existe una película con código {codigo}.")


def opcion_baja(ruta_peliculas, ruta_visualizaciones):
    """Opción 5: muestra la película y sus visualizaciones, pide confirmación y da de baja en cascada."""
    codigo = pedir_entero_positivo("Ingrese el código de la película a eliminar: ")
    pelicula = buscar_pelicula(ruta_peliculas, codigo)
    if len(pelicula) > 0:
        mostrar_pelicula(pelicula)
        cantidad = contar_visualizaciones(ruta_visualizaciones, codigo)
        print(f"\nVisualizaciones relacionadas que también se eliminarán: {cantidad}")
        if pedir_confirmacion("¿Confirma la baja? (S/N): "):
            baja_en_cascada(ruta_peliculas, ruta_visualizaciones, codigo)
            print(f"Película {codigo} y sus {cantidad} visualizaciones eliminadas.")
        else:
            print("Baja cancelada. No se modificó ningún archivo.")
    else:
        print(f"No existe una película con código {codigo}.")


def opcion_listado_cruzado(ruta_peliculas, ruta_visualizaciones):
    """Opción 6: muestra cada visualización con los datos de su película."""
    print("\nLISTADO CRUZADO DE VISUALIZACIONES\n")
    listar_cruzado(ruta_peliculas, ruta_visualizaciones)


def opcion_consulta_operaciones(ruta_peliculas, ruta_visualizaciones):
    """Opción 7: muestra la película, sus visualizaciones, la cantidad y los minutos acumulados."""
    codigo = pedir_entero_positivo("Ingrese el código de la película: ")
    pelicula = buscar_pelicula(ruta_peliculas, codigo)
    if len(pelicula) > 0:
        mostrar_pelicula(pelicula)
        cantidad, minutos = mostrar_operaciones(ruta_visualizaciones, codigo)
        mostrar_totales_operaciones(cantidad, minutos)
    else:
        print(f"No existe una película con código {codigo}.")


def opcion_estadisticas(ruta_peliculas, ruta_visualizaciones):
    """Opción 8: muestra las cuatro estadísticas (el promedio es de una película elegida)."""
    print(f"Cantidad total de visualizaciones: {total_visualizaciones(ruta_visualizaciones)}\n")
    print("Visualizaciones por película:")
    mostrar_visualizaciones_por_pelicula(ruta_peliculas, ruta_visualizaciones)
    maximo = maximo_visualizaciones(ruta_peliculas, ruta_visualizaciones)
    print("\nPelículas más visualizadas:")
    if maximo > 0:
        mostrar_mas_visualizadas(ruta_peliculas, ruta_visualizaciones, maximo)
    else:
        print("  No hay visualizaciones registradas.")
    codigo = pedir_entero_positivo("\nCódigo de película para calcular el promedio de minutos: ")
    pelicula = buscar_pelicula(ruta_peliculas, codigo)
    if len(pelicula) > 0:
        cantidad = contar_visualizaciones(ruta_visualizaciones, codigo)
        minutos = minutos_acumulados(ruta_visualizaciones, codigo)
        if cantidad > 0:
            promedio = promedio_minutos(minutos, cantidad)
            print(f"Promedio para {codigo}: {minutos} / {cantidad} = {promedio:.2f} minutos")
        else:
            print(f"La película {codigo} no tiene visualizaciones: no se puede calcular el promedio.")
    else:
        print(f"No existe una película con código {codigo}.")


def opcion_informe(ruta_peliculas, ruta_visualizaciones, ruta_reporte):
    """Opción 9: genera (sobrescribe) el informe consolidado con la información actualizada."""
    pass

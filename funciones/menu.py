# Menú principal
from funciones.constantes import RUTA_PELICULAS, RUTA_VISUALIZACIONES, RUTA_REPORTE
from funciones.validaciones import pedir_entero_en_rango
from funciones.opciones_menu import opcion_listar, opcion_consultar, opcion_alta, opcion_modificar, opcion_baja, opcion_listado_cruzado, opcion_consulta_operaciones,opcion_estadisticas, opcion_informe


def mostrar_menu():
    """Imprime las opciones del menú."""
    print("\n" + "=" * 52)
    print("\n=== SISTEMA DE GESTIÓN DE CATÁLOGO ===")
    print("=" * 52)
    print("1. Listar películas")
    print("2. Consultar película por código")
    print("3. Alta de película")
    print("4. Modificar película")
    print("5. Baja de película y su historial ")
    print("6. Listado cruzado de visualizaciones")
    print("7. Consultar visualizaciones de una película")
    print("8. Estadísticas")
    print("9. Generar informe consolidado")
    print("0. Salir")


def ejecutar_opcion(opcion):
    """Ejecuta la opción elegida; si falta un archivo o no se puede acceder, informa y vuelve al menú."""
    try:
        if opcion == 1:
            opcion_listar(RUTA_PELICULAS)
        elif opcion == 2:
            opcion_consultar(RUTA_PELICULAS)
        elif opcion == 3:
            opcion_alta(RUTA_PELICULAS)
        elif opcion == 4:
            opcion_modificar(RUTA_PELICULAS)
        elif opcion == 5:
            opcion_baja(RUTA_PELICULAS, RUTA_VISUALIZACIONES)
        elif opcion == 6:
            opcion_listado_cruzado(RUTA_PELICULAS, RUTA_VISUALIZACIONES)
        elif opcion == 7:
            opcion_consulta_operaciones(RUTA_PELICULAS, RUTA_VISUALIZACIONES)
        elif opcion == 8:
            opcion_estadisticas(RUTA_PELICULAS, RUTA_VISUALIZACIONES)
        elif opcion == 9:
            opcion_informe(RUTA_PELICULAS, RUTA_VISUALIZACIONES, RUTA_REPORTE)
    except FileNotFoundError as error:
        print("ERROR. No se encontró un archivo de datos necesario.")
        print("Detalle:", error)
    except OSError as error:
        print("ERROR. No fue posible acceder a los archivos.")
        print("Detalle:", error)


def iniciar_menu():
    """Repite mostrar menú, pedir opción y ejecutarla hasta que el usuario elija 0 (Salir)."""
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = pedir_entero_en_rango("Elija una opción: ", 0, 9)
        if opcion != 0:
            ejecutar_opcion(opcion)
            input("\nPresione ENTER para volver al menú...")
    print("\n¡Hasta luego!")


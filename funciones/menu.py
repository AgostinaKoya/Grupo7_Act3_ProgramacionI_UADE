# Menú principal
from funciones.constantes import RUTA_PELICULAS, RUTA_VISUALIZACIONES
from funciones.validaciones import pedir_entero_en_rango
from funciones.opciones_menu import opcion_listar, opcion_consultar, opcion_alta, opcion_modificar
from funciones.opciones_menu import opcion_baja, opcion_listado_cruzado, opcion_consulta_operaciones
from funciones.opciones_menu import opcion_estadisticas, opcion_informe


def mostrar_menu():
    """Imprime las opciones del menú."""
    print("\n" + "=" * 52)
    print("\n=== SISTEMA DE GESTIÓN DE CATÁLOGO ===")
    print("=" * 52)
    print("1. Ingresar película")
    print("2. Consultar película")
    print("3. Modificar película")
    print("4. Eliminar película y su historial")
    print("5. Listar catálogo")
    print("6. Listar visualizaciones")
    print("7. Consultar visualizaciones por película")
    print("8. Estadísticas") #No estoy seguro de que esta opción se necesite.
    print("9. Generar reporte de visualizaciones")
    print("0. Salir")


def ejecutar_opcion(opcion):
    #Modificar nombres de funciones
    """Llama a la función de la opción elegida pasándole las rutas de los archivos."""
    if opcion == 1:
        opcion_alta(matriz)
    elif opcion == 2:
        opcion_consultar(matriz)
    elif opcion == 3:
        opcion_modificar(matriz)
    elif opcion == 4:
        opcion_baja(matriz)
    elif opcion == 5:
        opcion_listar(matriz)
    elif opcion == 6:
        opcion_listado_cruzado(matriz)
    elif opcion == 7:
        opcion_consulta_operaciones(matriz)
    elif opcion == 8:
        opcion_estadisticas(matriz)
    elif opcion == 9:
        opcion_informe(matriz)


def iniciar_menu():
    """Repite mostrar menú, pedir opción y ejecutarla hasta que el usuario elija salir."""
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = pedir_entero_en_rango("Elija una opción: ", 0, 8)
        try:
            print(ejecutar_opcion(opcion, matriz)) #quitar el print para probar
        finally:
            if opcion != 0:
                input("\nPresione ENTER para volver al menú...")
    print("\n¡Hasta luego!")


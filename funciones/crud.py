# Lógica de alta, modificación y baja sobre las matrices (no pide datos ni imprime)
import os
from funciones.constantes import CODIGO, COD_PELICULA, RUTA_TEMP_PELICULAS, RUTA_TEMP_VISUALIZACIONES


def alta_pelicula(ruta_peliculas, codigo, titulo, genero, duracion, calificacion):
    """Agrega una película al final de peliculas.txt"""
    with open(ruta_peliculas, "a", encoding="UTF-8") as archivo:
        archivo.write(f"{codigo};{titulo};{genero};{duracion};{calificacion}\n")        


def modificar_pelicula(ruta_peliculas, codigo, titulo, genero, duracion, calificacion):
    """Reescribe peliculas.txt con los nuevos datos de la película indicada usando un archivo temporal."""
    with open(ruta_peliculas, "r", encoding="UTF-8") as original, \
         open(RUTA_TEMP_PELICULAS, "w", encoding="UTF-8") as temporal:
        for linea in original:
            datos = linea.strip().split(";")
            if int(datos[CODIGO]) == codigo:
                temporal.write(f"{codigo};{titulo};{genero};{duracion};{calificacion}\n")
            else:
                temporal.write(linea)
    os.replace(RUTA_TEMP_PELICULAS, ruta_peliculas)


    # encontrado = False

    # try:
    #     with open(ruta_peliculas, "r", encoding="UTF-8") as archivo:
    #         linea = archivo.readline()
    #         while linea !="" and not encontrado:
    #             datos = linea.strip().split(";")
    #             if int(datos[0]) == codigo_pelicula:
    #                 encontrado = True
    #             else:
    #                 linea = archivo.readline()  


    # except FileNotFoundError:
    #     print("ERROR. No se encontró el archivo.")
    # except OSError as error:
    #     print("ERROR. No fue posible acceder al archivo.")
    #     print("Detalle:", error)
        
    # else:
    #     if encontrado:
    #         titulo = datos[TITULO]
    #         genero = datos[GENERO]
    #         duracion = datos[DURACION]
    #         calificacion = datos[CALIFICACION]
    #         print(f'Registro encontrado: {codigo_pelicula} - {titulo} -  {genero} - {duracion} - {calificacion}')

    #         print("\nIngrese los nuevos valores (Enter para conservar el actual):")
    #         titulo_nuevo = pedir_texto_opcional("Título", titulo)
    #         genero_nuevo = pedir_texto_opcional("Género", genero) 
    #         duracion_nuevo = pedir_entero_opcional("Duración", int(duracion))

    #         calificacion_nuevo = pedir_entero_rango_opcional("Calificación", int(calificacion), 0, 5)
                
    #         print(f'Registro nuevo: {codigo_pelicula} - {titulo_nuevo} -  {genero_nuevo} - {duracion_nuevo} - {calificacion_nuevo}')

    #         try:
    #             with open(ruta_peliculas, "r", encoding="UTF-8") as archivo, open("temp.txt", "w", encoding="UTF-8") as temporal:
    #                 for linea in archivo:
    #                     datos = linea.strip().split(";")
    #                     if int(datos[0]) == codigo_pelicula:
    #                         registro = f'{codigo_pelicula};{titulo_nuevo};{genero_nuevo};{duracion_nuevo};{calificacion_nuevo}\n'
    #                         temporal.write(registro)
    #                     else: 
    #                         temporal.write(linea)
    #             os.replace("temp.txt",ruta_peliculas)
    #             print("Persona modificada correctamente")
                
    #         except OSError as error:
    #             print("ERROR. No fue posible modificar el archivo.")
    #             print("Detalle:", error)

    #     else:
    #         print("No se encotraron registros")




def baja_en_cascada(ruta_peliculas, ruta_visualizaciones, codigo):
    """Elimina la película de peliculas.txt y todas sus visualizaciones de visualizaciones.txt."""
    with open(ruta_peliculas, "r", encoding="UTF-8") as original, \
         open(RUTA_TEMP_PELICULAS, "w", encoding="UTF-8") as temporal:
        for linea in original:
            datos = linea.strip().split(";")
            if int(datos[CODIGO]) != codigo:
                temporal.write(linea)
    with open(ruta_visualizaciones, "r", encoding="UTF-8") as original, \
         open(RUTA_TEMP_VISUALIZACIONES, "w", encoding="UTF-8") as temporal:
        for linea in original:
            datos = linea.strip().split(";")
            if int(datos[COD_PELICULA]) != codigo:
                temporal.write(linea)
    os.replace(RUTA_TEMP_PELICULAS, ruta_peliculas)
    os.replace(RUTA_TEMP_VISUALIZACIONES, ruta_visualizaciones)
    
    # """Elimina la película y todas sus visualizaciones; devuelve las dos matrices actualizadas."""
    # nueva_lista_peliculas = []
    # nueva_lista_visualizaciones = []


    # for pelicula in peliculas:
    #     if pelicula[CODIGO] != codigo:
    #         nueva_lista_peliculas.append(pelicula)
    # #print(nueva_lista_peliculas)

    # for visualizacion in visualizaciones:
    #     if visualizacion[COD_PELICULA] != codigo:
    #         nueva_lista_visualizaciones.append(visualizacion)

    # return nueva_lista_peliculas, nueva_lista_visualizaciones
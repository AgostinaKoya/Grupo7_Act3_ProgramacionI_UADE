# Lógica de alta, modificación y baja sobre las matrices (no pide datos ni imprime)
import os

from funciones.constantes import CODIGO, TITULO, GENERO, DURACION, CALIFICACION, COD_PELICULA
from funciones.consultas import buscar_pelicula
from funciones.validaciones import pedir_texto_opcional, pedir_entero_opcional, pedir_entero_rango_opcional


def alta_pelicula(ruta_peliculas, codigo, titulo, genero, duracion, calificacion):
    """Agrega una película al final de peliculas.txt"""

    try: 
        with open(ruta_peliculas, "a", encoding="UTF-8") as archivo:
            archivo.write(f"{codigo};{titulo};{genero};{duracion};{calificacion}\n")        
    except FileNotFoundError:
        print("ERROR. No se encontró el archivo.")
    except OSError as error:
        print("ERROR. No fue posible acceder al archivo.")
        print("Detalle:", error)





def modificar_pelicula(ruta_peliculas, codigo_pelicula):

    encontrado = False

    try:
        with open(ruta_peliculas, "r", encoding="UTF-8") as archivo:
            linea = archivo.readline()
            while linea !="" and not encontrado:
                datos = linea.strip().split(";")
                if int(datos[0]) == codigo_pelicula:
                    encontrado = True
                else:
                    linea = archivo.readline()  


    except FileNotFoundError:
        print("ERROR. No se encontró el archivo.")
    except OSError as error:
        print("ERROR. No fue posible acceder al archivo.")
        print("Detalle:", error)
        
    else:
        if encontrado:
            titulo = datos[TITULO]
            genero = datos[GENERO]
            duracion = datos[DURACION]
            calificacion = datos[CALIFICACION]
            print(f'Registro encontrado: {codigo_pelicula} - {titulo} -  {genero} - {duracion} - {calificacion}')

            print("\nIngrese los nuevos valores (Enter para conservar el actual):")
            titulo_nuevo = pedir_texto_opcional("Título", titulo)
            genero_nuevo = pedir_texto_opcional("Género", genero) 
            duracion_nuevo = pedir_entero_opcional("Duración", int(duracion))

            calificacion_nuevo = pedir_entero_rango_opcional("Calificación", int(calificacion), 0, 5)
                
            print(f'Registro nuevo: {codigo_pelicula} - {titulo_nuevo} -  {genero_nuevo} - {duracion_nuevo} - {calificacion_nuevo}')

            try:
                with open(ruta_peliculas, "r", encoding="UTF-8") as archivo, open("temp.txt", "w", encoding="UTF-8") as temporal:
                    for linea in archivo:
                        datos = linea.strip().split(";")
                        if int(datos[0]) == codigo_pelicula:
                            registro = f'{codigo_pelicula};{titulo_nuevo};{genero_nuevo};{duracion_nuevo};{calificacion_nuevo}\n'
                            temporal.write(registro)
                        else: 
                            temporal.write(linea)
                os.replace("temp.txt",ruta_peliculas)
                print("Persona modificada correctamente")
                
            except OSError as error:
                print("ERROR. No fue posible modificar el archivo.")
                print("Detalle:", error)

        else:
            print("No se encotraron registros")




def baja_en_cascada(peliculas, visualizaciones, codigo):
    """Elimina la película y todas sus visualizaciones; devuelve las dos matrices actualizadas."""
    nueva_lista_peliculas = []
    nueva_lista_visualizaciones = []


    for pelicula in peliculas:
        if pelicula[CODIGO] != codigo:
            nueva_lista_peliculas.append(pelicula)
    #print(nueva_lista_peliculas)

    for visualizacion in visualizaciones:
        if visualizacion[COD_PELICULA] != codigo:
            nueva_lista_visualizaciones.append(visualizacion)

    return nueva_lista_peliculas, nueva_lista_visualizaciones
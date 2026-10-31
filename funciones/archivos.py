# Lectura y escritura de los archivos de texto (no importa otros módulos)

def buscar_pelicula(ruta_peliculas, codigo):
    """Recorre todo el archivo hasta encontrar el código, si encuentra devuelve una lista de la pelicula, sino devuelve una lista vacía"""
    encontrado = False
    
    try:
        with open(ruta_peliculas, "r", encoding="UTF-8") as archivo:
            linea = archivo.readline()

            while linea != "" and not encontrado:
                datos = linea.strip().split(";")

                if int(datos[0]) == codigo:
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
            return datos

    return [] #aca tuve que hacer que devuelva [] porque sino me devuelve la última linea del archivo.
                #capaz podemos devolver None




def contar_visualizaciones(ruta_visualizaciones, codigo):
    """Recorre todo el archivo y cuenta las líneas de esa película"""
    contador = 0

    try:
        with open(ruta_visualizaciones, "r", encoding="UTF-8") as archivo:
            linea = archivo.readline()

            while linea != "":
                datos = linea.strip().split(";")

                if int(datos[1]) == codigo:
                    contador += 1

                linea = archivo.readline()

    except FileNotFoundError:
        print("ERROR. No se encontró el archivo.")

    except OSError as error:
        print("ERROR. No fue posible acceder al archivo.")
        print("Detalle:", error)

    return contador


def minutos_acumulados(ruta_visualizaciones, codigo):
    """Recorre todo el archivo y suma los minutos de esa película"""
    suma = 0

    try:
        with open(ruta_visualizaciones, "r", encoding="UTF-8") as archivo:
            linea = archivo.readline()

            while linea != "":
                datos = linea.strip().split(";")

                if int(datos[1]) == codigo:
                    suma += int(datos[2])

                linea = archivo.readline()

    except FileNotFoundError:
        print("ERROR. No se encontró el archivo.")
    except OSError as error:
        print("ERROR. No fue posible acceder al archivo.")
        print("Detalle:", error)

    return suma


def leer_ultimo_codigo(ruta_peliculas):
    """Recorre peliculas.txt y devuelve el código de la última película (0 si el archivo está vacío)."""
    ultimo = 0

    try:
        with open(ruta_peliculas, "r", encoding="UTF-8") as archivo:
            for linea in archivo:
                if linea.strip() != "":
                    datos = linea.strip().split(";")
                    ultimo = int(datos[0])
    except FileNotFoundError:
        print("ERROR. No se encontró el archivo.")
    except OSError as error:
        print("ERROR. No fue posible acceder al archivo.")
        print("Detalle:", error)
    return ultimo


# def leer_peliculas(ruta):
#     """Lee peliculas.txt y devuelve la matriz de películas; si no existe informa y devuelve None."""
#     archivo = None
#     peliculas = []

#     try:
#         archivo = open(ruta,"r", encoding="UTF-8" )
#     except FileNotFoundError:
#         print("ERROR. El archivo no existe.")
#     except OSError as error:
#         print("ERROR. No fue posible abrir el archivo.")
#         print("Detalle:", error)   
#     else:
#         for linea in archivo:
#             datos = linea.strip().split(";")
#             codigo = int(datos[0])
#             descripcion = datos[1]
#             genero = datos[2]
#             duracion = int(datos[3])
#             clasificacion = int(datos[4])            
#             pelicula = [codigo, descripcion,genero,duracion,clasificacion]
#             peliculas.append(pelicula)
#     finally:
#         if archivo != None:
#             archivo.close()   
#         if not peliculas:
#                 return None               

#     return peliculas


# def leer_visualizaciones(ruta):
#     """Lee visualizaciones.txt y devuelve la matriz de visualizaciones; si no existe informa y devuelve None."""
#     archivo = None
#     visualizaciones = []

#     try:
#         archivo = open(ruta,"r", encoding="UTF-8" )
#     except FileNotFoundError:
#         print("ERROR. El archivo no existe.")
#     except OSError as error:
#         print("ERROR. No fue posible abrir el archivo.")
#         print("Detalle:", error)   
#     else:
#         for linea in archivo:
#             datos = linea.strip().split(";")
#             nro_visualizacion = int(datos[0])
#             cod_pelicula = int(datos[1])
#             minutos = int(datos[2])            
#             visualizacion = [nro_visualizacion, cod_pelicula,minutos]
#             visualizaciones.append(visualizacion)
#     finally:
#         if archivo != None:
#             archivo.close()
#         if not visualizaciones:
#                 return None  

#     return visualizaciones


# def guardar_peliculas(ruta, peliculas):
#     """Reescribe peliculas.txt con la matriz actual; devuelve True si pudo guardar."""


# def guardar_visualizaciones(ruta, visualizaciones):
#     """Reescribe visualizaciones.txt con la matriz actual; devuelve True si pudo guardar."""
#     pass

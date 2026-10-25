# Lectura y escritura de los archivos de texto (no importa otros módulos)


def leer_peliculas(ruta):
    """Lee peliculas.txt y devuelve la matriz de películas; si no existe informa y devuelve None."""
    archivo = None
    peliculas = []

    try:
        archivo = open(ruta,"r", encoding="UTF-8" )
    except FileNotFoundError:
        print("ERROR. El archivo no existe.")
    except OSError as error:
        print("ERROR. No fue posible abrir el archivo.")
        print("Detalle:", error)   
    else:
        for linea in archivo:
            datos = linea.strip().split(";")
            codigo = int(datos[0])
            descripcion = datos[1]
            genero = datos[2]
            duracion = int(datos[3])
            clasificacion = int(datos[4])            
            pelicula = [codigo, descripcion,genero,duracion,clasificacion]
            peliculas.append(pelicula)
    finally:
        if archivo != None:
            archivo.close()   
        if not peliculas:
                return None               

    return peliculas


def leer_visualizaciones(ruta):
    """Lee visualizaciones.txt y devuelve la matriz de visualizaciones; si no existe informa y devuelve None."""
    archivo = None
    visualizaciones = []

    try:
        archivo = open(ruta,"r", encoding="UTF-8" )
    except FileNotFoundError:
        print("ERROR. El archivo no existe.")
    except OSError as error:
        print("ERROR. No fue posible abrir el archivo.")
        print("Detalle:", error)   
    else:
        for linea in archivo:
            datos = linea.strip().split(";")
            nro_visualizacion = int(datos[0])
            cod_pelicula = int(datos[1])
            minutos = int(datos[2])            
            visualizacion = [nro_visualizacion, cod_pelicula,minutos]
            visualizaciones.append(visualizacion)
    finally:
        if archivo != None:
            archivo.close()
        if not visualizaciones:
                return None  

                

    return visualizaciones

#Deberia sobreesccribir o hacer un append?
def guardar_peliculas(ruta, peliculas):
    """Reescribe peliculas.txt con la matriz actual; devuelve True si pudo guardar."""
    pass


def guardar_visualizaciones(ruta, visualizaciones):
    """Reescribe visualizaciones.txt con la matriz actual; devuelve True si pudo guardar."""
    pass

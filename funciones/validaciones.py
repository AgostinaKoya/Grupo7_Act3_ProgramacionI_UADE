# Validaciones y pedido de datos por teclado (no importa otros módulos)


def pedir_entero_positivo(mensaje):
    """Pide un entero mayor a 0, reintenta ante ValueError y devuelve el número."""
    valido = False
    while not valido:
        try: 
            numero = int(input(mensaje))
            while numero <=0:
                numero = int(input(mensaje))
            valido = True
        except ValueError:
            print("Error! Se esperaba un número, ingréselo")
       
    return numero


def pedir_entero_en_rango(mensaje, minimo, maximo):
    """Pide un entero entre minimo y maximo (calificación 1-5, opciones del menú) y lo devuelve."""
    valido = False
    while not valido:
        try: 
            numero = int(input(mensaje))
            if numero < minimo or numero > maximo:
                print(f"El valor debe estar entre {minimo} y {maximo}.")
            else:
                valido = True
        except ValueError:
            print("Error: se esperaba un número entero.")
    return numero


def pedir_texto_no_vacio(mensaje):
    """Pide un texto que no esté vacío (título, género) y lo devuelve."""
    valido = False
    while not valido:
        texto = input(mensaje).strip()
        if texto == "":
            print(f"El texto no debe estar vacío")
        else:
            valido = True
    return texto

def pedir_confirmacion(mensaje):
    """Pide confirmación S/N y devuelve True si el usuario confirma."""
    valido = False
    while not valido:
        confirmacion = input(mensaje).upper().strip()
        if confirmacion != "S" and confirmacion !="N" :
            print(f"Debe indicar S/N")
        elif confirmacion == "S":
            confirma = True
            valido = True
        elif confirmacion == "N":
            confirma = False
            valido = True
    return confirma

def pedir_texto_opcional(mensaje, actual):
    """Pide un texto nuevo; si el usuario presiona Enter devuelve el valor actual."""
    valido = False
    while not valido:
        texto = input(f"{mensaje} [{actual}]: ").strip()
        if texto == "":
            texto = actual
            valido = True
        elif ";" in texto:
            print("Error: el texto no puede contener ';'.")
        else:
            valido = True
    return texto

def pedir_entero_opcional(mensaje, actual):
    """Pide un entero; si el usuario presiona Enter devuelve el valor actual."""
    valido = False

    while not valido:
        entrada = input(f"{mensaje} [{actual}]: ").strip()

        if entrada == "":
            numero = actual
            valido = True
        else:
            try:
                numero = int(entrada)
                valido = True
            except ValueError:
                print("Error: debe ingresar un número entero.")

    return numero

def pedir_entero_rango_opcional(mensaje, actual, minimo, maximo):
    """Pide un entero entre minimo y maximo; si el usuario presiona Enter devuelve el valor actual."""
    valido = False
    while not valido:
        entrada = input(f"{mensaje} [{actual}]: ").strip()
        if entrada == "":
            numero = actual
            valido = True
        else:
            try:
                numero = int(entrada)
                if numero < minimo or numero > maximo:
                    raise ValueError(f"El valor debe estar entre {minimo} y {maximo}.")
                valido = True
            except ValueError as error:
                if "invalid literal" in str(error):
                    print("Error: debe ingresar un número entero.")
                else:
                    print(f"Error: {error}")
    return numero

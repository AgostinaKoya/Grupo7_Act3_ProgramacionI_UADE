# Validaciones y pedido de datos por teclado (no importa otros módulos)


def pedir_entero_positivo(mensaje):
    """Pide un entero mayor a 0; ante letras o valores menores o iguales a 0 informa y vuelve a pedir."""
    valido = False
    while not valido:
        try: 
            numero = int(input(mensaje))
            if numero <= 0:
                raise ValueError("El número debe ser mayor a 0.")
            valido = True
        except ValueError as error:
            if "invalid literal" in str(error):
                print("Error: debe ingresar un número entero, sin letras ni decimales.")
            else:
                print(f"Error: {error}")
    return numero


def pedir_entero_en_rango(mensaje, minimo, maximo):
    """Pide un entero entre minimo y maximo (calificación 1-5, opciones del menú) y lo devuelve."""
    valido = False
    while not valido:
        try: 
            numero = int(input(mensaje).strip())
            if numero < minimo or numero > maximo:
                raise ValueError(f"El valor debe estar entre {minimo} y {maximo}.")
            valido = True
        except ValueError as error:
            if "invalid literal" in str(error):
                print("Error: se esperaba un número entero.")
            else:
                print(f"Error: {error}")
    return numero


def pedir_texto_no_vacio(mensaje):
    """Pide un texto que no esté vacío y sin ';' (título, género) y lo devuelve."""
    valido = False
    while not valido:
        texto = input(mensaje).strip()
        if texto == "":
            print(f"Error: El texto no debe estar vacío")
        elif ";" in texto:
            print("Error: el texto no puede contener ';'.")
        else:
            valido = True
    return texto


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

def pedir_entero_opcional(mensaje, actual, minimo, maximo):
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


def pedir_confirmacion(mensaje):
    """Pide S/N hasta que la respuesta sea válida; devuelve True si el usuario confirma."""
    respuesta = input(mensaje).strip().upper()
    while respuesta != "S" and respuesta != "N":
        print("Error: debe responder S o N.")
        respuesta = input(mensaje).strip().upper()
    return respuesta == "S"


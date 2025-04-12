class NumeroDebeSerPositivo(Exception):
    """Excepción lanzada cuando se ingresa un número negativo."""
    pass


def ingrese_numero():
    """
    Solicita al usuario ingresar un número y valida que sea positivo.
    
    Returns:
        int: El número ingresado si es válido.
        
    Raises:
        ValueError: Si la entrada no es un número válido.
        NumeroDebeSerPositivo: Si el número ingresado es negativo.
    """
    entrada = input("Ingrese un número positivo: ")
    try:
        numero = int(entrada)
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número entero válido")


def main():
    """
    Función principal que maneja el flujo del programa y las excepciones.
    """
    try:
        numero = ingrese_numero()
        print(f"¡Número válido ingresado: {numero}!")
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except NumeroDebeSerPositivo as ndsp:
        print(f"Error: {ndsp}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()
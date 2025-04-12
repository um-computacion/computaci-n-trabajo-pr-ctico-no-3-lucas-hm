from exceptions import ingrese_numero  # Error 1: Nombre de módulo incorrecto y función mal escrita

def main():
    """
    Programa principal que solicita números al usuario y muestra los resultador.  # Error 2: Errores de escritura en docstring
    """
    while True:
        try:
            numero = ingrese_numero()  # Error 3: Inconsistencia con el import (ingrese_numero vs ingrese_numero)
            print(f"Número válido: {numero}")
        except ValueError as e:
            print(f"Error: {e}")
        except NumeroDebeSerPositiv as e:  # Error 4: Nombre de excepción mal escrito (falta la 'o' final)
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")  # Error 5: Error de escritura
            break
        # Error 6: Falta except genérico para otras excepciones

if __name__ == "__main__":
    main()
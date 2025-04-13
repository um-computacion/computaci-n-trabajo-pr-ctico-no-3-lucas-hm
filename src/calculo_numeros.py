from typing import Optional
from exceptions import ingrese_numero

class NumeroDebeSerPositivo(Exception):
    """Excepción personalizada para números negativos."""
    pass


def obtener_numero_usuario() -> Optional[int]:
    """
    Solicita repetidamente un número al usuario hasta que ingrese uno válido o cancele.
    
    Returns:
        int: Número positivo ingresado por el usuario
        None: Si el usuario cancela la operación
        
    Raises:
        ValueError: Si la entrada no es un número válido
        NumeroDebeSerPositivo: Si el número es negativo
    """
    while True:
        try:
            entrada = input("Ingrese un número positivo (o Ctrl+C para salir): ")
            numero = int(entrada)
            if numero < 0:
                raise NumeroDebeSerPositivo("El número debe ser positivo")
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido")
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario")
            return None


def main():
    """
    Programa principal que maneja la entrada de números con gestión robusta de errores.
    """
    print("=== Validador de números positivos ===")
    
    while True:
        try:
            numero = obtener_numero_usuario()
            
            if numero is None:  # El usuario canceló
                break
                
            print(f"\n✅ Número válido ingresado: {numero}\n")
            
            # Opción para continuar o salir
            continuar = input("¿Desea ingresar otro número? (s/n): ").lower()
            if continuar != 's':
                print("\n¡Hasta luego!")
                break
                
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}\n")
            # Podríamos agregar logging aquí para producción
            break


if __name__ == "__main__":
    main()
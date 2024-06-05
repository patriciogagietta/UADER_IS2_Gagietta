"""

Copyright UADERFCyT-IS2©2024 todos los derechos reservados


"""
import json
import sys

class SingletonMeta(type):
    """
    La clase Singleton se puede implementar de diferentes formas en Python. Alguno
    Los métodos posibles incluyen: clase base, decorador, metaclase. Usaremos el
    metaclase porque es la más adecuada para este propósito.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Los posibles cambios en el valor del argumento `__init__` no afectan
        la instancia devuelta.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class RecuperacionToken(metaclass=SingletonMeta):
    """ 
        Clase para la recuperación de tokens desde un archivo JSON 
        que implementa el patrón de creacion singleton para asegurar que solo exista una instancia.
    """

    def __init__(self, jsonfile):
        self.saldo = {
            "token1": 1000,
            "token2": 2000
        }
        self.jsonfile = jsonfile

    def realizar_pago(self, monto):
        for token in self.saldo:
            if self.saldo[token] >= monto:
                self.saldo[token] -= monto
                print(f"Pago {monto} desde el token '{token}'")
                return
            
        print(f"No hay saldo en ninguna cuenta para realizar el pago de ${monto}")

    def recuperacion_token(self):
        try:
            with open(self.jsonfile, 'r') as myfile:
                data = myfile.read()
            obj = json.loads(data)

            # Si encuentra el valor lo devuelve, sino devuelve que no lo encontro
            return obj.get("token", "Token no encontrado")
        # Se produce cuando se intenta acceder a un archivo que no existe
        except FileNotFoundError:
            print("El archivo JSON no existe o lo ingreso de manera incorrecta")


if __name__ == "__main__":
    VERSION = "Versión 1.1"

    if len(sys.argv) < 2:
        print("No ingreso como argumento el archivo JSON")
        sys.exit(1)

    if "-v" in sys.argv:
        print(VERSION)
        print()


    JSONFILE = sys.argv[1]

    s1 = RecuperacionToken(JSONFILE)
    s2 = RecuperacionToken(JSONFILE)


    if id(s1) == id(s2):
        s1.realizar_pago(500)
        s1.realizar_pago(500)
        s1.realizar_pago(500)
        s1.realizar_pago(500)
        s1.realizar_pago(500)
        s1.realizar_pago(500)
        s1.realizar_pago(500)
        s1.realizar_pago(500)
        s1.realizar_pago(500)



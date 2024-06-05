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
    """ Clase para la recuperación de tokens desde un archivo JSON 
        que implementa el patrón de creacion singleton para asegurar que solo exista una instancia.
    """

    def recuperacion_token(self, jsonfile, jsonkey):
        try:
            with open(jsonfile, 'r') as myfile:
                data = myfile.read()
            obj = json.loads(data)

            # Si encuentra el valor lo devuelve, sino devuelve que no lo encontro
            print(str(obj.get(jsonkey, "Token no encontrado")))
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

    s1 = RecuperacionToken()
    s2 = RecuperacionToken()

    JSONFILE = sys.argv[1]

    if len(sys.argv) > 2:
        JSONKEY = sys.argv[2]
    else:
        JSONKEY = "token1"

    if id(s1) == id(s2):
        s1.recuperacion_token(JSONFILE,JSONKEY)

"""

Copyright UADERFCyT-IS2©2024 todos los derechos reservados


"""
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List, Dict

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
        self.historial_pagos = pagosCollection()

    def realizar_pago(self, monto, numero_pedido):
        for token in self.saldo:
            if self.saldo[token] >= monto:
                self.saldo[token] -= monto
                pago = {"Numero de pedido": numero_pedido, "Token": token, "Monto": monto}
                self.historial_pagos.add_pago(pago)
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

    def listado_pagos(self):
        return iter(self.historial_pagos)



class AlphabeticalOrderIterator(Iterator):
    """
    Los iteradores concretos implementan varios algoritmos transversales. estas clases
    memorizar en todo momento la posición de recorrido actual.
    """

    """
    El atributo `_position` almacena la posición transversal actual. Un iterador puede
    Tiene muchos otros campos para almacenar el estado de iteración, especialmente cuando
    se supone que funciona con un tipo particular de colección.
    """

    _position: int = None

    """
    Este atributo indica la dirección transversal.
    """
    _reverse: bool = False

    def __init__(self, collection: pagosCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        El método __next__() debe devolver el siguiente elemento de la secuencia. En
        llegando al final, y en llamadas posteriores, debe lanzar StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class pagosCollection(Iterable):
    """
    Las colecciones concretas proporcionan uno o varios métodos para recuperar material fresco.
    instancias de iterador, compatibles con la clase de colección.
    """
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        El método __iter__() devuelve el objeto iterador en sí; de forma predeterminada,
        devuelve el iterador en orden ascendente.
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_pago(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    VERSION = "Versión 1.2"

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

        s1.realizar_pago(500, 1)
        s1.realizar_pago(500, 2)
        s1.realizar_pago(500, 3)
        s1.realizar_pago(500, 4)
        s1.realizar_pago(500, 5)
        s1.realizar_pago(500, 6)
        s1.realizar_pago(500, 7)
        
        print()
        print("Historial de pagos:")
        for pago in s1.listado_pagos():
            print(pago)



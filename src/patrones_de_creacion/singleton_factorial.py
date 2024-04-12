#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Factorial(metaclass=SingletonMeta):

    def funcion_factorial(self, numero):
        if numero < 0:
            return
        elif numero == 0:
            return 1
        else:
            factorial = 1
            while (numero > 0):
                factorial *= numero
                numero -= 1
            return factorial




if __name__ == "__main__":
    # The client code.

    s1 = Factorial()
    s2 = Factorial()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
        print()

        numero = int(input("Ingrese un numero para calcular su factorial: "))
        print()
        
        if numero >= 0:
            print(f"El factorial de {numero} es {s1.funcion_factorial(numero)}")
        else:
            print("Ingreso un valor negativo o incorrecto")
    else:
        print("Singleton failed, variables contain different instances.")

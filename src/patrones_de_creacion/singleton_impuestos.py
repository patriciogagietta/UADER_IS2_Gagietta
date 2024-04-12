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


class Impuestos(metaclass=SingletonMeta):
    def impuesto_IVA(self):
        return 0.21
    
    def impuesto_IIBB(self):
        return 0.05
    
    def impuesto_constribuciones_municipales(self):
        return 0.012

if __name__ == "__main__":
    # The client code.

    s1 = Impuestos()
    s2 = Impuestos()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
        print()
        base_imponible = float(input("Ingrese un valor de importe base imponible: "))
        print()
        print(f"Suma del impuesto IVA (21%) sobre el valor de importe base imponible ({base_imponible}): {s1.impuesto_IVA() * base_imponible + base_imponible}")
        print(f"Suma del impuesto IIBB (5%) sobre el valor de importe base imponible ({base_imponible}): {s1.impuesto_IIBB() * base_imponible + base_imponible}")
        print(f"Suma del impuesto Contribuciones municipales (1,2%) sobre el valor de importe base imponible ({base_imponible}): {s1.impuesto_constribuciones_municipales() * base_imponible + base_imponible}")
    else:
        print("Singleton failed, variables contain different instances.")

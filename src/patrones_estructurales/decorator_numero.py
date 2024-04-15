#*--------------------------------------------------
#* decorator.py
#* excerpt from https://refactoring.guru/design-patterns/decorator/python/example
#*--------------------------------------------------

class Component():
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    def operation(self) -> str:
        pass


class Numero(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """

    def __init__(self, numero: int) -> None:
        self._numero = numero

    def operation(self) -> str:
        return self._numero


class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class Suma(Decorator):
    def operation(self) -> str:
        return f"Suma: {self.component.operation() + 2}"


class Multiplicaion(Decorator):
    def operation(self) -> str:
        return f"Multiplicacion: {self.component.operation() * 2}"
    
class Division(Decorator):
    def operation(self) -> str:
        return f"Divicion: {self.component.operation() / 3}"


def client_code(component: Component) -> None:
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """ 

    # ...

    print(f"{component.operation()}", end="")

    # ...


if __name__ == "__main__":

    numero = Numero(int(input("Ingrese un numero: ")))
    print(f"Numero")
    client_code(numero)
    print("\n")

    suma = Suma(numero)
    client_code(suma)
    print()

    multiplicacion = Multiplicaion(numero)
    client_code(multiplicacion)
    print()

    division = Division(numero)
    client_code(division)

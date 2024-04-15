from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.
    """

    def __init__(self, implementation: Lamina) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return self.implementation.operation_implementation()


class Lamina(ABC):

    def __init__(self, ancho: float, espesor: float) -> None:
        self.ancho = ancho
        self.espesor = espesor

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class Laminas5metros(Lamina):
    def operation_implementation(self) -> str:
        return f"Produciendo laminas de 5 metros con {self.ancho} metros de ancho y {self.espesor} de espesor."


class Laminas10metros(Lamina):
    def operation_implementation(self) -> str:
        return f"Produciendo laminas de 10 metros con {self.ancho} metros de ancho y {self.espesor} de espesor."


if __name__ == "__main__":

    laminas_5_metros = Laminas5metros(0.5, 1.5)
    abstraction1 = Abstraction(laminas_5_metros)
    print(abstraction1.operation())

    laminas_10_metros = Laminas10metros(0, 2.5)
    abstraction2 = Abstraction(laminas_10_metros)
    print(abstraction2.operation())

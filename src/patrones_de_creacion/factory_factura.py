#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        factura = self.factory_method()

        # Now, use the product.
        result = f"Factura - Valor $500: {factura.operation()}\n"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteIvaResponsable(Creator):
    def factory_method(self) -> Factura:
        return IvaResponsable()


class ConcreteIvaNoInscripto(Creator):
    def factory_method(self) -> Factura:
        return IvaNoInscripto()
    
class ConcreteIvaExento(Creator):
    def factory_method(self) -> Factura:
        return IvaExento()


class Factura(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class IvaResponsable(Factura):
    def operation(self) -> str:
        return "IVA Responsable"


class IvaNoInscripto(Factura):
    def operation(self) -> str:
        return "IVA No Inscripto"
    
class IvaExento(Factura):
    def operation(self) -> str:
        return "IVA Exento"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long ascreator.some_operation() the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"{creator.some_operation()}", end="")


if __name__ == "__main__":

    condicion_cliente = input("Ingrese su condicion impositiva: ")

    if condicion_cliente == "responsable":
        client_code(ConcreteIvaResponsable())
    elif condicion_cliente == "no inscripto":
        client_code(ConcreteIvaNoInscripto())
    elif condicion_cliente == "exento":
        client_code(ConcreteIvaExento())
    else:
        print("Ingreso una condicion impositiva incorrecta, opciones: responsable-no inscripto-exento")    

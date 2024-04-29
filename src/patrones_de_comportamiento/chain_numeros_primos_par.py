from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_par(numero):
    return numero % 2 == 0

class Primo(AbstractHandler):
    def handle(self, request: int) -> str:
        if es_primo(request):
            return "Numero primo lo consume"
        else:
            return super().handle(request)


class Par(AbstractHandler):
    def handle(self, request: int) -> str:
        if es_par(request):
            return "Numero par lo consume"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for i in range(1, 101):
        print("\n")
        print(f"Numero: {i}")

        result = handler.handle(i)
        if result:
            print(f"    {result}", end="")
        else:
            print("     no se consumio", end="")


if __name__ == "__main__":

    numero_par = Par()
    numero_primo = Primo()

    numero_par.set_next(numero_primo)
    client_code(numero_par)
    # print("\n")

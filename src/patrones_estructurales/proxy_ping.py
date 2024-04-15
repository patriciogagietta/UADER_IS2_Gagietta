#*--------------------------------------------------
#* proxy.py
#* excerpt from https://refactoring.guru/design-patterns/proxy/python/example
#*--------------------------------------------------

from abc import ABC, abstractmethod
import os

class Ping(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def execute(self, string: str) -> None:
        pass

    @abstractmethod
    def executefree(self, string: str) -> None:
        pass


class RealPing(Ping):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """

    def execute(self, string: str) -> None:
        if string.startswith("192."):       # se verifica si la ip empieza con 192.
            for i in range(10):
                respuesta = os.system(f"ping {string}")  
        else:
            print("La IP no empieza con 192")

    def executefree(self, string: str) -> None:
        for i in range(10):
            respuesta = os.system(f"ping {string}")        


class PingProxy(Ping):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, ping: Ping) -> None:
        self._ping = ping

    def execute(self, string: str) -> None:
        if string == "192.168.0.254":
            self._ping.executefree("www.google.com")
        else:
            self._ping.execute(string)

    def executefree(self, string: str) -> None:
        self._ping.executefree(string)


def client_code(ping: Ping, string: str) -> None:
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.
    """

    # ...

    ping.execute(string)

    # ...


if __name__ == "__main__":
    # instancias de RealPing y PingProxy
    real_ping = RealPing()
    proxy = PingProxy(real_ping)

    ip_192 = "192.168.0.255"
    print("Ping a una direccion que enpieza con 192")
    client_code(real_ping, ip_192)

    ip_google = "192.168.0.254"
    print("Ping a google")
    client_code(proxy, ip_google)

    ip_sin_192 = "190.168.0.1"
    print("Ping a una direccion que no empieza con 192")
    client_code(real_ping, ip_sin_192)

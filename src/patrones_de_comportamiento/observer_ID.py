from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Sujeto: subscripción.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Sujeto: Notificación a los observadores ...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self, ID) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("Sujeto: Estoy haciendo algo importante.")
        self._state = ID

        print(f"Sujeto: Mi estado acaba de cambiar a: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class Suscriptor1(Observer):
    def __init__(self, subscriptor_1):
        self.subscriptor_1 = subscriptor_1

    def update(self, subject: Subject) -> None:
        if subject._state == self.subscriptor_1:
            print(f"Subscriptor1 - ID: {self.subscriptor_1}: coincide con el ID emitido")


class Suscriptor2(Observer):
    def __init__(self, subscriptor_2):
        self.subscriptor_2 = subscriptor_2

    def update(self, subject: Subject) -> None:
        if subject._state == self.subscriptor_2:
            print(f"Subscriptor2 - ID: {self.subscriptor_2}: coincide con el ID emitido")


class Suscriptor3(Observer):
    def __init__(self, subscriptor_3):
        self.subscriptor_3 = subscriptor_3

    def update(self, subject: Subject) -> None:
        if subject._state == self.subscriptor_3:
            print(f"Suscriptor3 - ID: {self.subscriptor_3}: coincide con el ID emitido")


class Suscriptor4(Observer):
    def __init__(self, subscriptor_4):
        self.subscriptor_4 = subscriptor_4

    def update(self, subject: Subject) -> None:
        if subject._state == self.subscriptor_4:
            print(f"Subscriptor4 - ID: {self.subscriptor_4}: coincide con el ID emitido")


if __name__ == "__main__":
    # The client code.
    subject = ConcreteSubject()

    subscriptor_1 = "9808"
    subscriptor_2 = "3421"
    subscriptor_3 = "3442"
    subscriptor_4 = "9000"

    id1 = "3421"
    id2 = '8752'
    id3 = '9808'
    id4 = '7891'
    id5 = '3442'
    id6 = '2391'
    id7 = '9879'
    id8 = '9000'

    observer_1 = Suscriptor1(subscriptor_1)
    subject.attach(observer_1)

    observer_2 = Suscriptor2(subscriptor_2)
    subject.attach(observer_2)

    observer_3 = Suscriptor3(subscriptor_3)
    subject.attach(observer_3)

    observer_4 = Suscriptor4(subscriptor_4)
    subject.attach(observer_4)

    subject.some_business_logic(id1)
    subject.some_business_logic(id2)
    subject.some_business_logic(id3)
    subject.some_business_logic(id4)
    subject.some_business_logic(id5)
    subject.some_business_logic(id6)
    subject.some_business_logic(id7)
    subject.some_business_logic(id8)
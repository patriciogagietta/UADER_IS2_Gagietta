from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """

        pass


class Pieza(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """

    def operation(self) -> str:
        return "Pieza"


class Composite(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Producto({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """

    print(f"RESULTADO: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple or
    complex, without depending on their concrete classes.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":

    print("Creando el producto principal")
    producto_principal = Composite()
    client_code(producto_principal)
    print("\n")

    print("Creando el primer subconjunto con sus 4 piezas")
    sub_conjunto1 = Composite()
    # Agregar las 4 piezas al subconjunto
    for i in range(4):
        sub_conjunto1.add(Pieza())
    client_code(sub_conjunto1)
    print("\n")

    print("Creando el segundo subconjunto con sus 4 piezas")
    sub_conjunto2 = Composite()
    # Agregar las 4 piezas al subconjunto
    for i in range(4):
        sub_conjunto2.add(Pieza())
    client_code(sub_conjunto2)
    print("\n")

    print("Creando el tercer subconjunto con sus 4 piezas")
    sub_conjunto3 = Composite()
    # Agregar las 4 piezas al subconjunto
    for i in range(4):
        sub_conjunto3.add(Pieza())
    client_code(sub_conjunto3)
    print("\n")

    # Se agregan los subconjuntos al producto principal
    producto_principal.add(sub_conjunto1)
    producto_principal.add(sub_conjunto2)
    producto_principal.add(sub_conjunto3)

    print("Producto principal")
    client_code(producto_principal)
    print("\n")

    print("Creando el subconjunto adicional con sus 4 piezas")
    sub_conjunto4 = Composite()
    # Agregar las 4 piezas al subconjunto
    for _ in range(4):
        sub_conjunto4.add(Pieza())
    client_code(sub_conjunto4)
    print("\n")

    producto_principal.add(sub_conjunto4)

    print("Producto principal compuesto con un subconjunto adicional")
    client_code(producto_principal)

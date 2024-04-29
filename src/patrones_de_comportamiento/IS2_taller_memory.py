

import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		
		self.file = file
		self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = []
        self.states = []

    def write(self, string):
        self.content.append(string)

    def save(self):
        copied_content = [str(item) for item in self.content]
        memento = Memento(self.file, copied_content)
        self.states.append(memento)

    def undo(self, memento, index=0):
        index = int(input("Ingrese los estados que quiere recuperar: "))

        if index < len(self.states):
            print("Se invoca undo para recuperar los estados asignados")
            memento = self.states[-1 - index]
            self.file = memento.file
            for i in range(index):
                self.content.pop()
        else:
              print("No hay suficientes estados para recuperar")



class FileWriterCaretaker:

	def save(self, writer):
		self.obj = writer.save()

	def undo(self, writer):
		writer.undo(self.obj)


if __name__ == '__main__':
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")
    print()

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content)
    caretaker.save(writer)
    print()

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones")
    print(writer.content)
    caretaker.save(writer)
    print()

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II")
    print(writer.content)
    print()

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones III")
    print(writer.content)
    print()

    caretaker.undo(writer)
    print("Se muestra el estado actual")
    print(writer.content)
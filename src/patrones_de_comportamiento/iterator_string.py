class Iterator():
    def __init__(self, string):
        self._string = string
        self._index = 0

    def __next__(self):
        try:
            result = self._string[self._index]
            self._index += 1
            return result
        except IndexError:
            raise StopIteration


class StringCollection():
    def __init__(self, string):
        self._string = string

    def __iter__(self):
        return Iterator(self._string)


if __name__ == "__main__":
    string = input("Ingrese una palabra: ")
    string_collection = StringCollection(string)

    print("Recorrido en sentido directo:")
    for letra in string_collection:
        print(letra, end="")

    print("\n")

    print("Recorrido en sentido reverso:")
    for letra in reversed(string_collection._string):
        print(letra, end="")

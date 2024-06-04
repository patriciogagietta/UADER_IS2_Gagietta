import json, sys

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class RecuperacionToken(metaclass=SingletonMeta):

    def recuperacion_token(self, jsonfile, jsonkey):
        try:
            with open(jsonfile, 'r') as myfile:
                data = myfile.read()
            obj = json.loads(data)

            print(str(obj.get(jsonkey, "Token no encontrado")))                                 # Si encuentra el valor lo devuelve, sino devuelve que no lo encontro
        except FileNotFoundError:                                                      # Se produce cuando se intenta acceder a un archivo que no existe
            print("El archivo JSON no existe o lo ingreso de manera incorrecta")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("No ingreso como argumento el archivo JSON")
        sys.exit(1)

    s1 = RecuperacionToken()
    s2 = RecuperacionToken()

    jsonfile = sys.argv[1]

    if len(sys.argv) > 2:
        jsonkey = sys.argv[2]   
    else:
        jsonkey = "token1"    


    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
        print()

        s1.recuperacion_token(jsonfile,jsonkey)
    else:
        print("Singleton failed, variables contain different instances.")

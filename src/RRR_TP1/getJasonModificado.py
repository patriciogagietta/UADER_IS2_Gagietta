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

        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)

        print(str(obj[jsonkey]))


if __name__ == "__main__":

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

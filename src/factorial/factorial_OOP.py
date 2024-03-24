#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*


import sys

class Factorial:
    def __init__(self):
        pass

    def factorial(self, num): 
        if num < 0: 
            print("Factorial de un número negativo no existe")

        elif num == 0: 
            return 1
            
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 
        
    def run(self,minimo,maximo):
        for i in range(minimo, maximo + 1):
            print("Factorial ",i,"! es ", self.factorial(i))

factorial = Factorial()

# para comprobar si paso los numeros minimo y maximo como argumento
if len(sys.argv) < 3:
    minimo = int(input("Numero minimo para calcular su factorial: "))
    maximo = int(input("Numero maximo para calcular su factorial: "))
else:
    minimo = int(sys.argv[1])
    maximo = int(sys.argv[2])

# llamamos al metodo run definido dentro de la clase que calcula el factorial dentro del rango pasado como argumento
factorial.run(minimo,maximo)
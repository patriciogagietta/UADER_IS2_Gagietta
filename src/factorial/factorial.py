#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
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

# para comprobar si paso los numeros minimo y maximo como argumento
if len(sys.argv) < 2:
    maximo = int(input("Numero maximo para calcular su factorial: "))
else:
    maximo = int(sys.argv[1])

for i in range(1, maximo + 1):
    print("Factorial ",i,"! es ", factorial(i))
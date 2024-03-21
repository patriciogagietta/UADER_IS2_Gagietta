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
    

# para comprobar si paso el numero como argumento
if len(sys.argv) < 2:
    num = input("Debe ingresar un numero para calcular su factorial: ")
    num = int(num)
else:
    num = int(sys.argv[1])

print("Factorial ",num,"! es ", factorial(num))
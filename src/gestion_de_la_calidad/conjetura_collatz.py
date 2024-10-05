#Calculando el número de iteraciones del algoritmo de Collatz
def collatz(num):
    iteraciones = 0

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3*num + 1

        iteraciones += 1

    return iteraciones
#Comprobando los resultados

while True:
    try:
        i = int(input("Ingrese un numero: "))
        
        if ((i > 0) and (i <= 1999)):
            break
        elif (i < 0):
            print("Ingrese un numero mayor a 0")
        else:
            print("Ingrese un numero menor a 1999")
    except ValueError:
        print("Lo ingresado no es un numero entero positivo")
    print()


print("El número de iteraciones para %d es %d\n" % (i,collatz(i)))
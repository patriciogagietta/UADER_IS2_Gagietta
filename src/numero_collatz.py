import matplotlib.pyplot as plt

def collatz(num):
    iteraciones = 0
    num_inicial = num

    # ciclo para calcular la conjetura, si es numero par se divide por 2. si es impar se multiplica por 3 y se le suma 1. se van incrementando las iteraciones
    while(num != 1):
        if (num % 2 == 0):
            num = num / 2
        else:
            num = (num * 3) + 1

        iteraciones += 1

    return num_inicial,iteraciones

total_x = []
total_y = []

for i in range(1, 10001):
    num_inicial,iteraciones = collatz(i)

    total_x.append(iteraciones)
    total_y.append(num_inicial)

plt.plot(total_x,total_y,".")
plt.title("Numero de Collatz entre 1 y 10000") # agregar un titulo al grafico
plt.xlabel("Iteraciones") # cambiar titulo del grafico del eje x
plt.ylabel("Numero de comienzo") # cambiar titulo del grafico del eje y
plt.show() #para mostrar el grafico
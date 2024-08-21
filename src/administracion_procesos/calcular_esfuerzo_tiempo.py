import numpy as np
import matplotlib.pyplot as plt

# S es el tamaño del proceso que se pasa como parametro
def calcular_esfuerzo(S):
    return 8 * S ** 0.95

# E es el esfuerzo que retorno la funcion anterior
def calcular_tiempo_calendario(E):
    return 2.4 * E ** 0.33

# valores de los intervalos
tamaños_0_10000 = np.linspace(0, 10000, 100)
tamaños_1_500 = np.linspace(1, 500, 100)

# esfuerzos segun el tamaño de proyecto generados
esfuerzos_0_10000 = calcular_esfuerzo(tamaños_0_10000)
tiempos_calendario_1_500 = calcular_tiempo_calendario(tamaños_1_500)


# Graficos
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(tamaños_0_10000, esfuerzos_0_10000)
plt.xlabel('Tamaño del Proyecto')
plt.ylabel('Esfuerzo')
plt.title('Esfuerzo dependiendo del tamaño del proyecto')

plt.subplot(1, 2, 2)
plt.plot(tamaños_1_500, tiempos_calendario_1_500)
plt.xlabel('Esfuerzo')
plt.ylabel('Tiempo Calendario')
plt.title('Tiempo calendario dependiendo del esfuerzo')

plt.show()

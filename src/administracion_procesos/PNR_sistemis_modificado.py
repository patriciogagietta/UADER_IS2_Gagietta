import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Funciones de soporte

#*--- Calcula el esfuerzo instantaneo o staff p(t) en un momento t
def E(t, K, a):
   """Calcula el valor de la función E(t)"""
   return 2 * K * a * t * np.exp(-a * t**2)

#*--- Calcula el esfuerzo acumulado en función del tiempo E(t)
def E_acum(K, a, t):
   return K * (1 - np.exp(-a * (t**2)))

#*--- Estima el esfuero consumido al momento de la liberación del proyecto, el remanente será un residual para soporte post-instalación
def E_proyecto(K, a, gamma):  
   tf = np.sqrt(-np.log(1 - gamma) / a)
   Ef = gamma * K
   return tf, Ef

#*=*=*=*=*=*=*=* Funciones auxiliares de graficación

def esfuerzo_instantaneo(t, a, K):
   return 2 * K * a * t * np.exp(-a * t**2)

def esfuerzo_acumulado(t, a, K):
   return K * (1 - np.exp(-a * t**2))

# Cargar dataset histórico
t_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])        # Tiempo en meses
E_data = np.array([8, 21, 25, 30, 25, 24, 17, 15, 11])  # Esfuerzo instantáneo en persona-mes
K_historico = np.sum(E_data)  # Esfuerzo total histórico

# Calibrar modelo de mejor ajuste
popt, _ = curve_fit(esfuerzo_instantaneo, t_data, E_data, p0=[0.1, K_historico])
a_estimada, K_estimada = popt

# Solicitar valor del esfuerzo total en PM (personas-mes) para el nuevo proyecto
K_proyecto = float(input("Ingrese el esfuerzo del proyecto en personas-mes: "))

# Graficar datos históricos y modelo ajustado
t_fit = np.linspace(min(t_data), max(t_data), 100)
E_fit_historico = esfuerzo_instantaneo(t_fit, a_estimada, K_estimada)

plt.scatter(t_data, E_data, label='Datos históricos')
plt.plot(t_fit, E_fit_historico, label='Modelo ajustado', color='red')

# Graficar curva del proyecto con esfuerzo aceptado
E_fit_proyecto = esfuerzo_instantaneo(t_fit, a_estimada, K_proyecto)
plt.plot(t_fit, E_fit_proyecto, label=f'Proyecto con K={K_proyecto:.1f}', color='blue')

plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (personas-mes)')
plt.legend()
plt.show()

# Graficar el esfuerzo acumulado para el proyecto aceptado
E_acum_proyecto = esfuerzo_acumulado(t_fit, a_estimada, K_proyecto)
plt.plot(t_fit, E_acum_proyecto, label=f'Esfuerzo acumulado K={K_proyecto:.1f}', color='green')

plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo acumulado (personas-mes)')
plt.legend()
plt.show()

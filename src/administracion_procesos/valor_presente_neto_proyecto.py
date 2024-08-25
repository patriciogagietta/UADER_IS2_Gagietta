# variables
pago_mensual = 1000
tasa_anual = 0.01
n_meses_12 = 12
n_meses_15 = 15
v_presente_flujos_futuros = 18000


# funcion valor presente de los costos
def  v_presente_costos(meses):
    return pago_mensual * ((1 - (1 + tasa_anual) ** -meses) / tasa_anual)

# funcion valor presentes de los ingresos futuros
def  v_presente_ingresos_futuros(meses):
    return v_presente_flujos_futuros / ((1 + tasa_anual) ** meses)

# valores valor presente de los costos
v_presente_costos_12meses = v_presente_costos(n_meses_12)
v_presente_costos_15meses = v_presente_costos(n_meses_15)

# valores valor presente de los ingresos futuros
v_presente_ingresos_futuros_12meses = v_presente_ingresos_futuros(n_meses_12)
v_presente_ingresos_futuros_15meses = v_presente_ingresos_futuros(n_meses_15)

# valor presente neto del proyecto
v_presente_neto_12meses = v_presente_ingresos_futuros_12meses - v_presente_costos_12meses
v_presente_neto_15meses = v_presente_ingresos_futuros_15meses - v_presente_costos_15meses

# rentabilidad del proyecto para una inversion de 12 meses
rentabilidad_12meses = v_presente_neto_12meses / v_presente_costos_12meses

# rentabilidad del proyecto para una inversion de 15 meses
rentabilidad_15meses = v_presente_neto_15meses / v_presente_costos_15meses

print(f"valor presente neto del proyecto con inversion de 12 meses: ${v_presente_neto_12meses}")
print(f"valor presente neto del proyecto con inversion de 15 meses: ${v_presente_neto_15meses}")
print()
print(f"rentabilidad del proyecto para una inversion de 12 meses: {rentabilidad_12meses * 100}%")
print(f"rentabilidad del proyecto para una inversion de 15 meses: {rentabilidad_15meses * 100}%")
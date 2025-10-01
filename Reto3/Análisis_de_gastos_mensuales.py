# ANALISIS DE GASTOS MENSUALES - PYTHON CON CICLO FOR (Sin funciones, listas, ni diccionarios)

print("--- Análisis de Gastos Mensuales (Ciclo for) ---")

# 1. ENTRADA: Solicitar N meses a analizar y validar
while True:
    try:
        num_meses = int(input("Ingrese el número de meses a analizar (1 a 12): "))
        if 1 <= num_meses <= 12:
            break
        else:
            print("Por favor, ingrese un número entre 1 y 12.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

# 2. INICIALIZACIÓN DE VARIABLES
total_anual = 0.0

gasto_maximo = -1.0 # Inicializar con un valor muy bajo
mes_maximo = 0      # Almacena el número del mes (1, 2, 3, ...)

gasto_minimo = float('inf') # Inicializar con un valor muy grande
mes_minimo = 0

# 3. PROCESO: Ciclo for para iterar sobre los meses
# i es el índice (de 0 a N-1). mes_numero es la posición lógica (de 1 a N).
for i in range(num_meses):
    mes_numero = i + 1
    
    # Solicitud y validación de gasto para el mes actual
    while True:
        try:
            gasto = float(input(f"Ingrese el gasto para el Mes {mes_numero} (en pesos): "))
            if gasto >= 0:
                break
            else:
                print("El gasto no puede ser negativo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    # Acumular el total anual
    total_anual += gasto

    # Identificar el mes con mayor gasto
    if gasto > gasto_maximo:
        gasto_maximo = gasto
        mes_maximo = mes_numero

    # Identificar el mes con menor gasto (Extra)
    if gasto < gasto_minimo:
        gasto_minimo = gasto
        mes_minimo = mes_numero

# 4. CÁLCULOS FINALES
promedio_mensual = total_anual / num_meses
diferencia_max_min = gasto_maximo - gasto_minimo

# 5. SALIDA: Mostrar los resultados
print("\n--- Resultados del Análisis Anual ---")

print(f"Número de meses analizados: {num_meses}")
print(f"El gasto total del año fue: ${total_anual:,.2f}")
print(f"El promedio de gastos mensuales fue: ${promedio_mensual:,.2f}")
print(f"El mes con mayor gasto fue **Mes {mes_maximo}** con ${gasto_maximo:,.2f}")
print(f"El mes con menor gasto fue **Mes {mes_minimo}** con ${gasto_minimo:,.2f}")
print(f"La diferencia entre el mes de mayor y menor gasto fue: ${diferencia_max_min:,.2f}")
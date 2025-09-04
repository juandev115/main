import math

# --- Valores ---

consumo_diario_por_persona = 150 # litros/día 
num_personas = 80  # personas
capacidad_tanque = 10000  # litros
eficiencia = 0.90  # 90%
dias_mantenimiento = 10  # días inactivos
area_disponible = 300  # m²
area_por_tanque = 2.5  # m²

# --- Requerimientos ---

# 1. Calcular el consumo diario y anual total de agua. 
consumo_diario_total = consumo_diario_por_persona * num_personas
consumo_anual_total = consumo_diario_total * 365
print(f"Consumo diario total de agua: {consumo_diario_total:.2f} litros.")
print(f"Consumo anual total de agua: {consumo_anual_total:.2f} litros.")

# 2. Calcular la capacidad útil de un tanque. 
capacidad_util_tanque = capacidad_tanque * eficiencia
print(f"Capacidad útil de un tanque: {capacidad_util_tanque:.2f} litros.")

# 3. Determinar cuántos tanques son necesarios para cubrir el consumo. 
consumo_total_necesario = consumo_diario_total * (365 + dias_mantenimiento)
num_tanques_necesarios = math.ceil(consumo_total_necesario / capacidad_util_tanque)
print(f"Número de tanques necesarios: {num_tanques_necesarios}.")

# 4. Calcular el área total necesaria para instalar los tanques. 
area_total_necesaria = num_tanques_necesarios * area_por_tanque
print(f"Área total necesaria para los tanques: {area_total_necesaria:.2f} m².")

# Uso de un enfoque de formato de cadena para "evaluar" la suficiencia del área
estado_area = ("El área disponible es suficiente para la instalación." * (area_total_necesaria <= area_disponible) +
               "¡Atención! El área disponible no es suficiente." * (area_total_necesaria > area_disponible))
print(estado_area)

# --- Cálculos Adicionales (Extra) ---

print("\n--- Cálculos Adicionales (Extra) ---")

# 5. Calcular cuántos días de autonomía tendría el sistema. 
capacidad_total_almacenamiento = num_tanques_necesarios * capacidad_util_tanque
dias_autonomia = capacidad_total_almacenamiento / consumo_diario_total
print(f"El sistema tendría una autonomía de {dias_autonomia:.2f} días con los tanques llenos.")

# 6. Estimar cuántos litros por persona podrían asignarse en una sequía de 30 días. 
dias_sequia = 30
litros_por_persona_en_sequia = (capacidad_total_almacenamiento / dias_sequia) / num_personas
print(f"En una sequía de {dias_sequia} días, se podrían asignar {litros_por_persona_en_sequia:.2f} litros por persona por día.")
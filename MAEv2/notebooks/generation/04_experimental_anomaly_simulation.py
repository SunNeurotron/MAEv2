import numpy as np
import matplotlib.pyplot as plt
#--- Constantes y Parámetros de la Misión (ACES en la ISS) ---
G = 6.67430e-11 # m^3 kg^-1 s^-2
M_earth = 5.97219e24 # kg
R_earth = 6371e3 # m
h_orbit = 408e3 # m (altitud de la ISS)
c = 299792458 # m/s
#1. Calcular la Diferencia de Potencial Gravitatorio (ΔU)
U_earth = -G * M_earth / R_earth
U_satellite = -G * M_earth / (R_earth + h_orbit)
delta_U = U_satellite - U_earth
#2. Calcular la predicción de la Relatividad General (GR)
delta_f_GR_frac = delta_U / c**2
#3. Calcular la predicción del MAE con un valor hipotético de delta
delta_MAE_param = 0.05
delta_f_MAE_frac = delta_f_GR_frac * (1 + delta_MAE_param)
#4. Calcular la Anomalía Predicha por el MAE
anomalia_predicha_MAE = delta_f_MAE_frac - delta_f_GR_frac
#5. Calcular la Incertidumbre Experimental
#La misión ACES apunta a una precisión de 2 partes por millón (2e-6) del efecto total
incertidumbre_experimental = 2e-6 * abs(delta_f_GR_frac)
#6. Simular 10 mediciones experimentales
np.random.seed(42)
datos_simulados = anomalia_predicha_MAE + np.random.normal(0, incertidumbre_experimental, 10)
#--- Gráfico de Residuos ---
fig, ax = plt.subplots(figsize=(12, 8))
ax.axhline(0, color='navy', linestyle='--', label='Predicción de la Relatividad General (Anomalía = 0)')
ax.axhline(anomalia_predicha_MAE, color='darkred', linestyle='-', label=f'Predicción del MAE (Anomalía = {anomalia_predicha_MAE:.3e})')
ax.errorbar(range(1, 11), datos_simulados, yerr=incertidumbre_experimental,
fmt='ko', capsize=5, label='Datos Experimentales Simulados (con incertidumbre)')
ax.set_title('Prueba Experimental: Búsqueda de Anomalías al Corrimiento al Rojo', fontsize=16, pad=20)
ax.set_xlabel('Número de Medición Experimental', fontsize=12)
ax.set_ylabel('Anomalía Medida (Dato - Predicción GR)', fontsize=12)
ax.set_xticks(range(1, 11))
ax.tick_params(axis='both', which='major', labelsize=10)
ax.legend(fontsize=12, loc='upper left')
plt.tight_layout()
#Guardar figura en el directorio de assets
plt.savefig('MAEv2/assets/figures/fig_mae_v4_experimental_test.png')
print("Figura 'fig_mae_v4_experimental_test.png' generada exitosamente.")
#Imprimir los valores clave para el documento
print("\n--- Valores para la Prueba Experimental (ACES en la ISS) ---")
print(f"Diferencia de Potencial Gravitatorio (ΔU): {delta_U:.4e} J/kg")
print(f"Corrimiento al Rojo predicho por GR (Δf/f): {delta_f_GR_frac:.4e}")
print(f"Corrimiento al Rojo predicho por MAE (Δf/f con δ={delta_MAE_param}): {delta_f_MAE_frac:.4e}")
print(f"Anomalía predicha por el MAE (δ * ΔU/c²): {anomalia_predicha_MAE:.4e}")
print(f"Incertidumbre experimental esperada (σ): {incertidumbre_experimental:.4e}")

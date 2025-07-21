import numpy as np
import matplotlib.pyplot as plt

# --- Constantes y Parámetros ---
# Simulación de un rango de diferencias de potencial gravitatorio (ej. diferentes órbitas)
# (En unidades de 10^7 J/kg, típico para órbitas LEO a GEO)
delta_U_range = np.linspace(0, 6, 100) * 1e7
c = 299792458  # m/s

# Valor hipotético para la desviación predicha por el MAE (δ)
delta_MAE = 0.05

# --- Cálculos ---
# Predicción de la Relatividad General (GR)
delta_f_GR = (delta_U_range / c**2)

# Predicción del Modelo de Acción Estructural (MAE)
delta_f_MAE = delta_f_GR * (1 + delta_MAE)

# --- Gráfico ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(delta_U_range / 1e7, delta_f_GR * 1e10, 'b--', label='Predicción de la Relatividad General (δ = 0)', linewidth=2)
ax.plot(delta_U_range / 1e7, delta_f_MAE * 1e10, 'r-', label=f'Predicción del MAE (δ = {delta_MAE})', linewidth=2.5)

ax.set_title('Predicción Teórica: Corrimiento al Rojo Gravitacional', fontsize=16, pad=20)
ax.set_xlabel('Diferencia de Potencial Gravitatorio ΔU (x 10⁷ J/kg)', fontsize=12)
ax.set_ylabel('Diferencia Fraccional de Frecuencia Δf/f (x 10⁻¹⁰)', fontsize=12)
ax.legend(fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=10)
plt.tight_layout()

# Guardar figura en el directorio de assets
plt.savefig('MAEv2/assets/figures/fig_mae_v4_theoretical_prediction.png')

print("Figura 'fig_mae_v4_theoretical_prediction.png' generada exitosamente.")

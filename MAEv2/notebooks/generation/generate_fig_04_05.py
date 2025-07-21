import numpy as np
import matplotlib.pyplot as plt

# Simulación del Experimento del Límite de la Acción
np.random.seed(42)
t = np.linspace(0, 1, 100)
emisor_base = np.random.randn(100)
receptor_base = np.random.randn(100)
patron = 0.5 * np.sin(2 * np.pi * 5 * t)
emisor_forced = emisor_base + patron
receptor_induced = receptor_base + 0.15 * patron

fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(t, emisor_forced, label='Emisor (con patrón)')
ax1.plot(t, receptor_induced, label='Receptor (con eco inducido)')
ax1.set_title('Señales de Emisor y Receptor')
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Anomalía Temporal (Δt)')
ax1.legend()
ax1.grid(True)
fig1.savefig('MODELO_DE_ACCION_ESTRUCTURAL_MAE_Unified_Theory/02_THEORY_DEVELOPMENT_CHRONOLOGY/02_The_Nature_of_the_Second_and_Its_Space/fig_04_action_limit_signals.png')

corr = np.correlate(emisor_forced, receptor_induced, mode='full')
lags = np.arange(-len(emisor_forced) + 1, len(emisor_forced))

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(lags, corr)
ax2.set_title('Análisis de Correlación Cruzada')
ax2.set_xlabel('Desfase')
ax2.set_ylabel('Correlación')
ax2.axvline(0, color='r', linestyle='--', label='Desfase Cero')
ax2.legend()
ax2.grid(True)
fig2.savefig('MODELO_DE_ACCION_ESTRUCTURAL_MAE_Unified_Theory/02_THEORY_DEVELOPMENT_CHRONOLOGY/02_The_Nature_of_the_Second_and_Its_Space/fig_05_action_limit_correlation.png')

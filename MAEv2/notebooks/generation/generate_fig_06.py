import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Análisis de la "Textura del Tiempo Continuo (1 Hora)"
np.random.seed(42)
time = np.arange(3600)
data = 0.1 + 0.05 * np.sin(2 * np.pi * time / 300) + 0.00001 * time + np.random.normal(0, 0.01, 3600)
data[1800] += 0.2

plt.figure(figsize=(12, 6))
plt.plot(time, data)
plt.title('Análisis del AIE: La Textura del Tiempo Continuo (1 Hora)')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Cantidad de Espacio')
plt.axvspan(1800, 1801, color='red', alpha=0.5, label='Evento Anómalo')
plt.legend()
plt.grid(True)
plt.savefig('MODELO_DE_ACCION_ESTRUCTURAL_MAE_Unified_Theory/02_THEORY_DEVELOPMENT_CHRONOLOGY/02_The_Nature_of_the_Second_and_Its_Space/fig_06_texture_of_time.png')

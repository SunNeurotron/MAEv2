import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
t = np.linspace(0, 1, 500)
emisor = np.random.randn(500) + np.sin(2 * np.pi * 10 * t)
receptor = np.random.randn(500) + 0.3 * np.sin(2 * np.pi * 10 * t)

plt.figure(figsize=(10, 6))
plt.plot(t, emisor, label='Emisor')
plt.plot(t, receptor, label='Receptor')
plt.title('Señal de Anomalía del Emisor y Receptor')
plt.xlabel('Tiempo')
plt.ylabel('Anomalía')
plt.legend()
plt.grid(True)
plt.savefig('MODELO_DE_ACCION_ESTRUCTURAL_MAE_Unified_Theory/SIASAF_ANALYSIS_REPORTS/siasaf_fig_01_anomaly_signal.png')

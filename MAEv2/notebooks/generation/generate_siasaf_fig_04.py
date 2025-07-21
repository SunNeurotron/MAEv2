import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
emisor_base = np.random.randn(500)
receptor_base = np.random.randn(500)
t = np.linspace(0, 1, 500)
patron = np.sin(2 * np.pi * 10 * t)
emisor_forced = emisor_base + patron
receptor_induced = receptor_base + 0.3 * patron

corr_base = np.correlate(emisor_base, receptor_base, mode='full')
corr_induced = np.correlate(emisor_forced, receptor_induced, mode='full')
lags = np.arange(-len(emisor_base) + 1, len(emisor_base))

plt.figure(figsize=(10, 6))
plt.plot(lags, corr_base, label='Base')
plt.plot(lags, corr_induced, label='Inducida')
plt.title('Comparación de Correlación Cruzada')
plt.xlabel('Desfase')
plt.ylabel('Correlación')
plt.legend()
plt.grid(True)
plt.savefig('MODELO_DE_ACCION_ESTRUCTURAL_MAE_Unified_Theory/SIASAF_ANALYSIS_REPORTS/siasaf_fig_04_correlation_comparison.png')

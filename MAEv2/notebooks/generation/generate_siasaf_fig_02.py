import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

np.random.seed(0)
t = np.linspace(0, 1, 500)
emisor = np.random.randn(500) + np.sin(2 * np.pi * 10 * t)
receptor = np.random.randn(500) + 0.3 * np.sin(2 * np.pi * 10 * t)

emisor_fft = np.abs(fft(emisor))
receptor_fft = np.abs(fft(receptor))
freqs = np.fft.fftfreq(len(t), 1/500)

plt.figure(figsize=(10, 6))
plt.plot(freqs[:len(freqs)//2], emisor_fft[:len(emisor_fft)//2], label='Emisor')
plt.plot(freqs[:len(freqs)//2], receptor_fft[:len(receptor_fft)//2], label='Receptor')
plt.title('Análisis Espectral de las Señales')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.savefig('MODELO_DE_ACCION_ESTRUCTURAL_MAE_Unified_Theory/SIASAF_ANALYSIS_REPORTS/siasaf_fig_02_fft.png')

import numpy as np
import matplotlib.pyplot as plt

# Simulación de un Evento Ω Teórico vs. un Evento Ω Real
np.random.seed(42)
x = np.linspace(-5, 5, 100)
teorico = np.exp(-x**2)
real = teorico + np.random.normal(0, 0.05, 100) + np.random.normal(0, 0.1) * np.exp(-(x-2)**2)

plt.figure(figsize=(10, 6))
plt.plot(x, teorico, 'g--', label='Evento Ω Teórico')
plt.plot(x, real, 'b-', label='Evento Ω Real')
plt.title('Captura de un Único Evento Ω')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.savefig('MODELO_DE_ACCION_ESTRUCTURAL_MAE_Unified_Theory/02_THEORY_DEVELOPMENT_CHRONOLOGY/02_The_Nature_of_the_Second_and_Its_Space/fig_01_omega_event_capture.png')

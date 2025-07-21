import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Comparación del "Segundo Tranquilo" vs. el "Segundo Agitado"
np.random.seed(42)
tranquilo = pd.DataFrame(np.random.rand(100, 2) * 0.1, columns=['x', 'y'])
agitado = pd.DataFrame(np.random.rand(100, 2), columns=['x', 'y'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.scatter(tranquilo['x'], tranquilo['y'])
ax1.set_title(f'Espacio del Segundo Tranquilo\nCantidad = {tranquilo.var().sum():.4f}')
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax2.scatter(agitado['x'], agitado['y'])
ax2.set_title(f'Espacio del Segundo Agitado\nCantidad = {agitado.var().sum():.4f}')
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
plt.suptitle('Comparación Cuantitativa de Dos Espacios')
plt.savefig('MODELO_DE_ACCION_ESTRUCTURAL_MAE_Unified_Theory/02_THEORY_DEVELOPMENT_CHRONOLOGY/02_The_Nature_of_the_Second_and_Its_Space/fig_03_space_quantity_comparison.png')

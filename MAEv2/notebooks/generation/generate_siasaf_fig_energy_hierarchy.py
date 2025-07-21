import matplotlib.pyplot as plt
import numpy as np

# Energías calculadas en el desarrollo
energia_pureza = 7.3017e-31
energia_ignicion = 6.0911e-24
energia_reduccion = 8.8037e-20

# Nombres de las energías
labels = ['Pureza (Mantener Orden)', 'Ignición (Crear Acción)', 'Reducción (Borrar Historia)']
energies = [energia_pureza, energia_ignicion, energia_reduccion]
log_energies = np.log10(energies)

# Colores para las barras
colors = ['cyan', 'orange', 'red']

# Crear el gráfico
plt.figure(figsize=(12, 8))
bars = plt.bar(labels, log_energies, color=colors)
plt.ylabel('Log10(Energía en Joules)')
plt.title('SIASAF: Verificación de la Jerarquía de Energías del Segundo (Escala Logarítmica)')
plt.grid(axis='y', linestyle='--')

# Añadir etiquetas de valor a las barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval - 2, f'10^{yval:.1f} J', va='center', ha='center', color='black', bbox=dict(facecolor='white', alpha=0.5))

# Guardar la figura
plt.savefig('MODELO_DE_ACCION_ESTRUCTURAL_MAE_Unified_Theory/SIASAF_ANALYSIS_REPORTS/siasaf_fig_energy_hierarchy.png')

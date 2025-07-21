import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generación y gráfica del "Espacio de Características de los Eventos Ω"
np.random.seed(42)
X = np.random.rand(100, 2)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.title('Espacio de Características de los Eventos Ω')
plt.xlabel('Anomalía Temporal (Δt)')
plt.ylabel('Anomalía de Amplitud (ΔA)')
plt.grid(True)
plt.savefig('MODELO_DE_ACCION_ESTRUCTURAL_MAE_Unified_Theory/02_THEORY_DEVELOPMENT_CHRONOLOGY/02_The_Nature_of_the_Second_and_Its_Space/fig_02_feature_space.png')

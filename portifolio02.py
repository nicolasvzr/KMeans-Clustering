import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


X = np.array([[4, 21],
              [5, 19],
              [10, 24],
              [4, 17],
              [3, 16],
              [11, 25],
              [14, 24],
              [6, 22],
              [10, 21],
              [12, 21]])

kMeans = KMeans(n_clusters=2, random_state=42) 
kMeans.fit(X)

labels = kMeans.labels_  
centroids = kMeans.cluster_centers_ 

# Plotando os clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', label="Pontos")  # Pontos coloridos pelos clusters
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, c='red', label="Centroides")  # Centroides destacados
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title(' Clustering com K-means')
plt.legend()
plt.show()
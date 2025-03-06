import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from kneed import KneeLocator


###Para a nossa base de dados, crie as seguintes matrizes:
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

conjunto_pontos = []

for k in range (1,11):
    kMeans = KMeans(n_clusters=k, random_state=42) 
    kMeans.fit(X)
    conjunto_pontos.append(kMeans.inertia_)


plt.plot(range(1,11), conjunto_pontos)
plt.xlabel('Numero de Clusters')
plt.ylabel('conjunto_pontos')
plt.title('Desenvolver um algoritmo k-means')
plt.show()

kl = KneeLocator(range(1, 11), conjunto_pontos, curve='convex', direction='decreasing')
N_cluster= kl.elbow
print(f'Número de Clusters: {N_cluster}')




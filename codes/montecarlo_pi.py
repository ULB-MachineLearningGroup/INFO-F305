import numpy as np
import matplotlib.pyplot as plt

n_points = 10000
approximations = []
points = (2*np.random.rand(n_points, 2))-1
inside_cirle = (np.array(points[:, 0])**2 + np.array(points[:, 1])**2) <= 1
aire = (np.sum(inside_cirle) / n_points) * 4
plt.figure(figsize=(10, 10))
plt.scatter(points[inside_cirle, 0], points[inside_cirle, 1], marker='.', label='Dans le cercle')
plt.scatter(points[~inside_cirle, 0], points[~inside_cirle, 1], marker='.', label='Hors du cercle')
plt.title(f"Valeur estimée de pi: {aire:.5f}")
plt.legend(loc="upper left")
plt.show()
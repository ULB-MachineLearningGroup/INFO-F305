import numpy as np
import matplotlib.pyplot as plt

n_points = 10000
approximations = []
points = np.random.rand(n_points, 2)
under_curve = np.array(points[:, 1]) <= np.array(points[:, 0])**2
estimation = np.sum(under_curve) / n_points
plt.figure(figsize=(10, 10))
plt.scatter(points[under_curve, 0], points[under_curve, 1], marker='.', label='Sous la courbe')
plt.scatter(points[~under_curve, 0], points[~under_curve, 1], marker='.', label='Au-dessus de la courbe')
plt.title(f"Valeur estimée de l'intégrale: {estimation:.5f}")
plt.legend(loc="upper left")
plt.show()
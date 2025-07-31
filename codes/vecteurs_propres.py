import numpy as np
import matplotlib.pyplot as plt

def vecteurs_propres(A):
    L, V = np.linalg.eig(A)
    line_range = np.linspace(-1.5, 1.5, 100)
    V = np.real(V)
    if V[0, 0] != 0:
        eigenvector_1 = (V[1,0] / V[0, 0]) * line_range
    if V[0, 1] != 0:
        eigenvector_2 = (V[1,1] / V[0, 1]) * line_range
    if V[0, 0] != 0 and V[0, 1] != 0:
        plt.quiver([0, 0], [0, 0], V[0, :], V[1, :], scale=10, width=0.005, color='red', label="Vecteurs propres")

plt.figure(figsize=(12, 12))
vecteurs_propres(np.array([[1, -2], [-2, 1]]))
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid()
plt.tight_layout()
plt.savefig("vecteurs_propres.svg", dpi=200)
plt.show()
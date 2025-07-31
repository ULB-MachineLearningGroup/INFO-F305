import numpy as np
import matplotlib.pyplot as plt

def vecteurs_vitesse(A):
    x1, x2 = np.meshgrid(np.arange(-1.5, 1.6, 0.1), np.arange(-1.5, 1.6, 0.1))
    
    x1_values = A[0,0]*x1 + A[0,1]*x2
    x2_values = A[1,0]*x1 + A[1,1]*x2
    
    norms = np.sqrt(x1_values**2 + x2_values**2)
    x1_normalized = x1_values / norms
    x2_normalized = x2_values / norms
    
    vector_scale = 40
    plt.quiver(x1, x2, x1_normalized, x2_normalized, scale=vector_scale)

plt.figure(figsize=(12, 12))
vecteurs_vitesse(np.array([[1, -2], [-2, 1]]))
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid()
plt.tight_layout()
plt.show()